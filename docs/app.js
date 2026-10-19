/* ============================================================
   app.js — 순수 바닐라 JS (외부 라이브러리 없음)
   ============================================================ */
(function () {
  "use strict";

  /* 연도 자동 */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  /* 네비게이션 활성 표시 (스크롤 위치 기준) */
  var links = Array.prototype.slice.call(document.querySelectorAll(".nav__links a"));
  var map = {};
  links.forEach(function (a) {
    var id = a.getAttribute("href").slice(1);
    var sec = document.getElementById(id);
    if (sec) map[id] = a;
  });
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.remove("is-active"); });
          var active = map[e.target.id];
          if (active) active.classList.add("is-active");
        }
      });
    }, { rootMargin: "-45% 0px -50% 0px", threshold: 0 });
    Object.keys(map).forEach(function (id) {
      io.observe(document.getElementById(id));
    });
  }

  /* 이메일 복사 버튼 */
  document.querySelectorAll(".contact__copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var val = btn.getAttribute("data-copy") || btn.textContent;
      var done = function () {
        var old = btn.textContent;
        btn.textContent = "복사됨";
        btn.classList.add("is-copied");
        setTimeout(function () { btn.textContent = old; btn.classList.remove("is-copied"); }, 1400);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(val).then(done, done);
      } else { done(); }
    });
  });

  /* ── 로컬(localhost)에서만 테마 비교 UI 표시 ── */
  var isLocal = ["localhost", "127.0.0.1"].indexOf(location.hostname) !== -1;
  if (isLocal) {
    var themes = [
      { id: "nightlime",  swatch: "#b7ed64", bg: "#0b1220" },
      { id: "slateamber", swatch: "#ffb454", bg: "#10141c" },
      { id: "monoink",    swatch: "#e6e8ec", bg: "#0d0f12" }
    ];
    var root = document.documentElement;
    var box = document.createElement("div");
    box.className = "theme-switch";
    box.setAttribute("aria-label", "테마 비교 (로컬 전용)");
    themes.forEach(function (t) {
      var b = document.createElement("button");
      b.type = "button";
      b.title = t.id;
      b.style.background = t.bg;
      b.style.boxShadow = "inset 0 0 0 3px " + t.swatch;
      if (root.getAttribute("data-theme") === t.id) b.classList.add("is-active");
      b.addEventListener("click", function () {
        root.setAttribute("data-theme", t.id);
        box.querySelectorAll("button").forEach(function (x) { x.classList.remove("is-active"); });
        b.classList.add("is-active");
      });
      box.appendChild(b);
    });
    document.body.appendChild(box);
  }
})();
