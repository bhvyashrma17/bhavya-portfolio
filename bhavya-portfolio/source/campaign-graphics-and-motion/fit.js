// Fit [data-fit] lines to the width of their parent's content box (or data-w px).
// data-max caps the font size. Runs once fonts are ready.
(function () {
  function fitAll() {
    document.querySelectorAll('[data-fit]').forEach(function (el) {
      var p = el.parentElement, cs = getComputedStyle(p);
      var avail = el.dataset.w ? +el.dataset.w : p.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
      el.style.whiteSpace = 'nowrap';
      el.style.display = 'inline-block';
      var lo = +(el.dataset.min || 8), hi = +(el.dataset.max || 900);
      for (var i = 0; i < 24; i++) {
        var mid = (lo + hi) / 2;
        el.style.fontSize = mid + 'px';
        if (el.getBoundingClientRect().width <= avail) lo = mid; else hi = mid;
      }
      el.style.fontSize = Math.floor(lo * 10) / 10 + 'px';
      if (el.dataset.block !== 'no') el.style.display = 'block';
      el.style.width = 'max-content';
    });
    document.documentElement.dataset.fitted = '1';
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitAll); else fitAll();
})();
