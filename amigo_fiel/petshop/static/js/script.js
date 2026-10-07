// AMIGO FIEL — script.js

// Marca a página como "com JS" (o CSS só esconde o .reveal se isso existir)
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", function () {
  // 1) Funcionalidade exigida: botão que dispara um alert
  var botao = document.getElementById("btn-alert");
  if (botao) {
    botao.addEventListener("click", function () {
      alert("Obrigado por visitar o Amigo Fiel! 🐾");
    });
  }

  // 2) Microinteração: seções entram suavemente ao aparecer na tela
  var secoes = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window)) {
    secoes.forEach(function (s) { s.classList.add("is-visible"); });
    return;
  }
  var observador = new IntersectionObserver(function (entradas) {
    entradas.forEach(function (entrada) {
      if (entrada.isIntersecting) {
        entrada.target.classList.add("is-visible");
        observador.unobserve(entrada.target);
      }
    });
  }, { threshold: 0.12 });
  secoes.forEach(function (s) { observador.observe(s); });
});
