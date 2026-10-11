// Playwright, as test/rec/check_rec.js asks for it with require('playwright'), unchanged except for one switch:
// with PW_HEADED=1 every browser starts headed (on the Xvfb display of a build machine, where headless Firefox has no WebGL),
// and Firefox gets its fake camera. Put this directory first on NODE_PATH and set PW_REAL to the real module's directory.
const real = require(process.env.PW_REAL);
const FF = { 'media.navigator.streams.fake': true, 'media.navigator.permission.disabled': true, 'webgl.force-enabled': true };
function wrap(type, name) {
  return new Proxy(type, {
    get(o, k) {
      if (k === 'launch') return (opts) => o.launch(Object.assign({}, opts, { headless: false }, name === 'firefox' ? { firefoxUserPrefs: Object.assign({}, FF, (opts || {}).firefoxUserPrefs) } : {}));
      const v = o[k]; return typeof v === 'function' ? v.bind(o) : v;
    }
  });
}
module.exports = new Proxy(real, {
  get(o, k) { return process.env.PW_HEADED === '1' && (k === 'firefox' || k === 'webkit' || k === 'chromium') ? wrap(o[k], k) : o[k]; }
});
