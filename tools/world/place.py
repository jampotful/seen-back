#!/usr/bin/env python3
"""Where the phone probably is, from its time zone and the creatures already met, and the prior over species that
follows (docs/tracks/worlddb.md, steps 2 and 3). The page carries out the same arithmetic (src/cam.place.js);
tools/world/test_place.py holds this file to its rules.

The world is a grid of `res`-degree cells. For each database row (a species) the file of records gives its research-grade
records through 2024 in each cell, count(c, s), and T(c) = sum over s is a cell's records.

  The local share. Round each cell c is a disc of radius r (400 km: the circle round the photo that held up for every
  list size, docs/COVERAGE.md): n_c(s) is the records of s in the cells whose centres lie within r of c's centre, and
  N_c the records of every species there. The share of s near c is
      share_c(s) = (n_c(s) + 1) / (N_c + S)                 (S: the number of rows)
  as tools/coverage/score.py has it for a circle: an unrecorded species is unlikely, never impossible.

  The first guess. P(c | zone) from tools/world/zones.py, mixed with the world: (1 - eps) P_zone(c) + eps P_world(c),
  P_world(c) proportional to T(c) + 1, so that a wrong first guess can still be overturned. No zone, or one the tables do
  not know: the world alone.

  The encounter rule. A creature the app names with confidence, species s, is evidence about the place:
      P(c | zone, s_1 .. s_k)  is proportional to  P(c | zone) * prod_i share_c(s_i)
  a Bayesian update over cells, kept on the device. Only creatures met in the phone's present zone count.

  The prior over species. share(s) = sum_c P(c) share_c(s); the page adds alpha * log share(s) to each row's score.
  Written out, sum_c P(c) (n_c(s) + 1) / (N_c + S) = sum_c' count(c', s) W(c') + sum_c w(c), with w(c) = P(c) / (N_c + S)
  and W the disc sums of w: one pass over the file of records.
"""
import math

import numpy as np

R_EARTH = 6371.0088


class Grid:
    def __init__(self, res):
        self.res = float(res)
        self.nr, self.nc = int(round(180 / res)), int(round(360 / res))
        self.n = self.nr * self.nc
        self.lat = -90 + (np.arange(self.nr) + 0.5) * self.res
        self.lon = -180 + (np.arange(self.nc) + 0.5) * self.res
        self._discs = {}

    def cell(self, lat, lon):
        r = np.clip(np.floor((np.asarray(lat, float) + 90) / self.res).astype(int), 0, self.nr - 1)
        c = np.clip(np.floor((np.asarray(lon, float) + 180) / self.res).astype(int), 0, self.nc - 1)
        return r * self.nc + c

    def half_widths(self, radius_km):
        """K[r, r2]: the cells of row r2 within radius of a cell of row r are those whose column differs by at most
        K[r, r2] (-1: none; nc: the whole row)."""
        if radius_km in self._discs:
            return self._discs[radius_km]
        p = np.radians(self.lat)
        K = np.full((self.nr, self.nr), -1, np.int64)
        dl = np.radians(np.arange(self.nc // 2 + 1) * self.res)
        for r in range(self.nr):
            # haversine between (lat_r, 0) and (lat_r2, dl) for every r2 and column step
            h = (np.sin((p[:, None] - p[r]) / 2) ** 2 + math.cos(p[r]) * np.cos(p)[:, None] * np.sin(dl[None, :] / 2) ** 2)
            d = 2 * R_EARTH * np.arcsin(np.sqrt(np.minimum(1, h)))
            ok = d <= radius_km
            any_ = ok.any(1)
            # the steps within the radius are the first ones, since distance grows with the step
            k = ok.sum(1) - 1
            k[~any_] = -1
            k[k >= self.nc // 2] = self.nc
            K[r] = k
        self._discs[radius_km] = K
        return K

    def disc_sum(self, values, radius_km):
        """For every cell, the sum of `values` (one a cell) over the cells within radius_km of its centre."""
        v = np.asarray(values, np.float64).reshape(self.nr, self.nc)
        K = self.half_widths(radius_km)
        nr, nc = self.nr, self.nc
        cs = np.concatenate([np.zeros((nr, 1)), np.cumsum(np.concatenate([v, v, v], axis=1), axis=1)], axis=1)
        tot = v.sum(1)
        out = np.zeros((nr, nc))
        cols = np.arange(nc)[None, :]
        span = int(np.ceil(radius_km / (111.19 * self.res))) + 1
        for dr in range(-span, span + 1):
            r = np.arange(max(0, -dr), min(nr, nr - dr))
            r2 = r + dr
            k = K[r, r2]
            ok = k >= 0
            if not ok.any():
                continue
            r, r2, k = r[ok], r2[ok], k[ok]
            whole = (k >= nc) | (2 * k + 1 >= nc)
            if whole.any():
                out[r[whole]] += tot[r2[whole]][:, None]
            p = ~whole
            if p.any():
                rp, r2p, kp = r[p], r2[p], k[p][:, None]
                out[rp] += cs[r2p[:, None], nc + cols + kp + 1] - cs[r2p[:, None], nc + cols - kp]
        return out.reshape(-1)


class Records:
    """count(c, s) a species at a time: offsets into cells and counts, rows in database order."""

    def __init__(self, grid, cells, rows, counts, S):
        self.grid, self.S = grid, int(S)
        o = np.lexsort((cells, rows))
        self.cells = np.asarray(cells, np.int64)[o]
        self.rows = np.asarray(rows, np.int64)[o]
        self.counts = np.asarray(counts, np.float64)[o]
        self.start = np.searchsorted(self.rows, np.arange(self.S + 1))
        self.T = np.bincount(self.cells, weights=self.counts, minlength=grid.n)

    def of(self, s):
        a, b = self.start[s], self.start[s + 1]
        return self.cells[a:b], self.counts[a:b]


class Place:
    def __init__(self, records, zones=None, alias=None, radius_km=400.0, eps=0.02):
        self.R, self.g = records, records.grid
        self.radius, self.eps = float(radius_km), float(eps)
        self.zones, self.alias = zones or {}, alias or {}
        self.N = self.g.disc_sum(self.R.T, self.radius)
        w = self.R.T + 1.0
        self.world = w / w.sum()

    def zone_name(self, name):
        if not name:
            return None
        if name in self.zones:
            return name
        a = self.alias.get(name)
        return a if a in self.zones else None

    def first_guess(self, zone):
        z = self.zone_name(zone)
        if z is None:
            return self.world.copy()
        cells, w = self.zones[z]
        P = self.eps * self.world
        np.add.at(P, np.asarray(cells, np.int64), (1 - self.eps) * np.asarray(w, np.float64))
        return P / P.sum()

    def local_counts(self, s):
        """n_c(s) for every cell."""
        cells, counts = self.R.of(s)
        v = np.zeros(self.g.n)
        np.add.at(v, cells, counts)
        return self.g.disc_sum(v, self.radius)

    def share_near(self, s):
        """share_c(s) for every cell."""
        return (self.local_counts(s) + 1.0) / (self.N + self.R.S)

    def update(self, P, s):
        """The encounter rule: P(c) times share_c(s), normalized."""
        L = np.log(self.share_near(s))
        lp = np.log(np.maximum(P, 1e-300)) + L
        lp -= lp.max()
        Q = np.exp(lp)
        return Q / Q.sum()

    def posterior(self, zone, met=()):
        P = self.first_guess(zone)
        for s in met:
            P = self.update(P, s)
        return P

    def log_share(self, P):
        """log share(s) for every row, share(s) = sum_c P(c) share_c(s)."""
        w = P / (self.N + self.R.S)
        W = self.g.disc_sum(w, self.radius)
        share = np.bincount(self.R.rows, weights=self.R.counts * W[self.R.cells], minlength=self.R.S) + w.sum()
        return np.log(share)


def circle_share(lat, lon, cells025, rows025, counts025, S, radius_km=400.0, starts025=None):
    """The true prior of a photo's place: (n(s) + 1) / (N + S) over the quarter-degree cells whose centres lie within
    radius_km of (lat, lon). cells025 must be sorted; starts025 (optional) is searchsorted(cells025, arange(720*1440+1))."""
    nr, nc, res = 720, 1440, 0.25
    lat0, lon0 = float(lat), float(lon)
    dlat = radius_km / 111.19 + res
    r0 = max(0, int((lat0 - dlat + 90) / res))
    r1 = min(nr - 1, int((lat0 + dlat + 90) / res))
    want = []
    p0 = math.radians(lat0)
    for r in range(r0, r1 + 1):
        la = -90 + (r + 0.5) * res
        p = math.radians(la)
        lo = -180 + (np.arange(nc) + 0.5) * res
        h = math.sin((p - p0) / 2) ** 2 + math.cos(p0) * math.cos(p) * np.sin(np.radians(lo - lon0) / 2) ** 2
        d = 2 * R_EARTH * np.arcsin(np.sqrt(np.minimum(1, h)))
        cc = np.nonzero(d <= radius_km)[0]
        if len(cc):
            want.append(r * nc + cc)
    n = np.zeros(S)
    if want:
        want = np.concatenate(want)
        if starts025 is None:
            starts025 = np.searchsorted(cells025, np.arange(nr * nc + 1))
        a, b = starts025[want], starts025[want + 1]
        idx = np.concatenate([np.arange(x, y) for x, y in zip(a, b) if y > x]) if (b > a).any() else np.zeros(0, np.int64)
        if len(idx):
            n = np.bincount(rows025[idx], weights=counts025[idx].astype(np.float64), minlength=S)
    return np.log((n + 1.0) / (n.sum() + S))
