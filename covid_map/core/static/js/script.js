const abaBrasil = document.querySelector("#aba-brasil");
const abaPiaui = document.querySelector("#aba-piaui");
const barraBrasil = document.querySelector("#barra-brasil");
const barraPiaui = document.querySelector("#barra-piaui");
const componentesBrasil = document.querySelectorAll("[componente-brasil]");
const componentesPiaui = document.querySelectorAll("[componente-piaui]");

function ativaBarraPiaui() {
  barraPiaui.style.display = "block";
  barraBrasil.style.display = "none";

  componentesBrasil.forEach(
    (componenteBrasil) => (componenteBrasil.style.display = "none")
  );
  componentesPiaui.forEach(
    (componentePiaui) => (componentePiaui.style.display = "block")
  );
}

function ativaBarraBrasil() {
  barraPiaui.style.display = "none";
  barraBrasil.style.display = "block";

  componentesBrasil.forEach(
    (componenteBrasil) => (componenteBrasil.style.display = "block")
  );
  componentesPiaui.forEach(
    (componentePiaui) => (componentePiaui.style.display = "none")
  );
}

abaBrasil.addEventListener("click", () => {
  ativaBarraBrasil();
});

abaPiaui.addEventListener("click", () => {
  ativaBarraPiaui();
});

// Menu Responsivo
let showMenu = true;

const menuToggle = document.querySelector(".menu-toggle");
const secaoMenu = document.querySelector(".secao-menu");

menuToggle.addEventListener("click", () => {
  document.body.style.overflow = showMenu ? "hidden" : "initial";

  secaoMenu.classList.toggle("on", showMenu);
  showMenu = !showMenu;
});
