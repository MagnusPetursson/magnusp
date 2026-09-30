/* magnusp.is: small enhancements, re-run after every instant-navigation page swap. */

(function () {
  /* The email address never appears in the HTML. Elements with class
     "mp-email" carry it base64-encoded and reversed in data-e; it is decoded
     and turned into a mailto link only in the browser. */
  function revealEmail(root) {
    root.querySelectorAll(".mp-email[data-e]").forEach(function (el) {
      var address = atob(el.dataset.e.split("").reverse().join(""));
      var link = document.createElement("a");
      link.href = "mailto:" + address;
      link.textContent = address;
      if (el.dataset.class) link.className = el.dataset.class;
      el.replaceWith(link);
    });
  }

  /* Contact form: submit in the background and report the result in place. */
  function wireForm(root) {
    var form = root.querySelector("form.mp-form");
    if (!form || form.dataset.wired) return;
    form.dataset.wired = "1";
    var status = form.querySelector(".mp-form__status");
    var button = form.querySelector("button[type=submit]");

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (form.querySelector("[name=_gotcha]").value) return; /* honeypot */
      button.disabled = true;
      status.textContent = form.dataset.sending;
      status.dataset.state = "";
      fetch(form.action, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" },
      })
        .then(function (response) {
          /* Formspree answers JSON; a non-2xx status means it rejected the message */
          if (!response.ok) throw new Error(response.status);
          form.reset();
          status.textContent = form.dataset.sent;
          status.dataset.state = "ok";
        })
        .catch(function () {
          status.textContent = form.dataset.failed;
          status.dataset.state = "error";
        })
        .finally(function () {
          button.disabled = false;
        });
    });
  }

  /* GoatCounter counts the first page load on its own. Pages opened through
     instant navigation don't reload, so count those here. */
  var firstPage = true;
  function countPageView() {
    if (firstPage) {
      firstPage = false;
      return;
    }
    if (window.goatcounter && window.goatcounter.count) {
      window.goatcounter.count({ path: location.pathname + location.search });
    }
  }

  function init() {
    revealEmail(document);
    wireForm(document);
    countPageView();
  }

  if (window.document$) {
    window.document$.subscribe(init);
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
