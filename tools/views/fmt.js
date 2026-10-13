'use strict';
// Short objects and arrays on one line, so a parameter reads as one line of the file.
function fmt(v, ind) {
  ind = ind || '';
  const flat = JSON.stringify(v);
  if (flat.length + ind.length <= 120 || v === null || typeof v !== 'object') return flat;
  const next = ind + '  ';
  if (Array.isArray(v)) return '[\n' + v.map(x => next + fmt(x, next)).join(',\n') + '\n' + ind + ']';
  return '{\n' + Object.keys(v).map(k => next + JSON.stringify(k) + ': ' + fmt(v[k], next)).join(',\n') + '\n' + ind + '}';
}
module.exports = { fmt };
