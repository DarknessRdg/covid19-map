const abaBrasil = document.querySelector("#aba-brasil");
const abaPiaui = document.querySelector("#aba-piaui");
const barraBrasil = document.querySelector("#barra-brasil");
const barraPiaui = document.querySelector("#barra-piaui");
const componentesBrasil = document.querySelectorAll("[componente-brasil]");
const componentesPiaui = document.querySelectorAll("[componente-piaui]");

// Abas (Gráfico) - BR
const abaGraficoBrConfirmados = document.querySelector(
  "#aba-grafico-br-confirmados"
);
const abaGraficoBrObitosAcumulados = document.querySelector(
  "#aba-grafico-br-obitos-acumulados"
);
const abaGraficoBrNovosObitos = document.querySelector(
  "#aba-grafico-br-novos-obitos"
);
const barraGraficoBrConfirmados = abaGraficoBrConfirmados.nextElementSibling;
const barraGraficoBrObitosAcumulados =
  abaGraficoBrObitosAcumulados.nextElementSibling;
const barraGraficoBrNovosObitos = abaGraficoBrNovosObitos.nextElementSibling;
const graficoBrConfirmados = document.querySelector("#grafico-br-confirmados");
const graficoBrNovosObitos = document.querySelector("#grafico-br-novos-obitos");
const graficoBrObitosAcumulados = document.querySelector(
  "#grafico-br-obitos-acumulados"
);

const graficosBr = [
  graficoBrConfirmados,
  graficoBrNovosObitos,
  graficoBrObitosAcumulados,
];

const barrasGraficoBr = [
  barraGraficoBrConfirmados,
  barraGraficoBrNovosObitos,
  barraGraficoBrObitosAcumulados,
];

// Abas (Mapa) - PI
const abaMapaPiConfirmados = document.querySelector("#aba-mapa-pi-confirmados");
const abaMapaPiObitos = document.querySelector("#aba-mapa-pi-obitos");
const barraAbaMapaPiConfirmados = abaMapaPiConfirmados.nextElementSibling;
const barraAbaMapaPiObitos = abaMapaPiObitos.nextElementSibling;
const mapaPiConfirmados = document.querySelector("#mapa-pi-confirmados");
const mapaPiObitos = document.querySelector("#mapa-pi-obitos");

// Abas (Gráfico) - PI

const abaGraficoPiConfirmados = document.querySelector(
  "#aba-grafico-pi-confirmados"
);
const abaGraficoPiObitos = document.querySelector("#aba-grafico-pi-obitos");
const abaGraficoPiDoencas = document.querySelector("#aba-grafico-pi-doencas");
const abaGraficoPiNovosCasos = document.querySelector(
  "#aba-grafico-pi-novos-casos"
);
const barraGraficoPiConfirmados = abaGraficoPiConfirmados.nextElementSibling;
const barraGraficoPiObitos = abaGraficoPiObitos.nextElementSibling;
const barraGraficoPiDoencas = abaGraficoPiDoencas.nextElementSibling;
const barraGraficoPiNovosCasos = abaGraficoPiNovosCasos.nextElementSibling;
const graficoPiConfirmados = document.querySelector("#grafico-pi-confirmados");
const graficoPiObitos = document.querySelector("#grafico-pi-obitos");
const graficoPiDoencas = document.querySelector("#grafico-pi-doencas");
const graficoPiNovosCasos = document.querySelector("#grafico-pi-novos-casos");

const graficosPi = [
  graficoPiConfirmados,
  graficoPiDoencas,
  graficoPiNovosCasos,
  graficoPiObitos,
];

const barrasGraficoPi = [
  barraGraficoPiConfirmados,
  barraGraficoPiDoencas,
  barraGraficoPiNovosCasos,
  barraGraficoPiObitos,
];

const menuToggle = document.querySelector(".menu-toggle");
const secaoMenu = document.querySelector(".secao-menu");


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

  graficoBrNovosObitos.style.display = "none";
  graficoBrObitosAcumulados.style.display = "none";
}

abaBrasil.addEventListener("click", () => {
  ativaBarraBrasil();
});

abaPiaui.addEventListener("click", () => {
  ativaBarraPiaui();
});

abaMapaPiConfirmados.addEventListener("click", () => {
  mapaPiObitos.style.display = "none";
  mapaPiConfirmados.style.display = "block";

  barraAbaMapaPiConfirmados.style.display = "block";
  barraAbaMapaPiObitos.style.display = "none";
});

abaMapaPiObitos.addEventListener("click", () => {
  mapaPiConfirmados.style.display = "none";
  mapaPiObitos.style.display = "block";

  barraAbaMapaPiConfirmados.style.display = "none";
  barraAbaMapaPiObitos.style.display = "block";
});


abaGraficoPiConfirmados.addEventListener("click", () => {
  graficoPiConfirmados.style.display = "block";
  barraGraficoPiConfirmados.style.display = "block";

  graficosPi.map((grafico) =>
    grafico !== graficoPiConfirmados ? (grafico.style.display = "none") : false
  );

  barrasGraficoPi.map((barra) =>
    barra !== barraGraficoPiConfirmados ? (barra.style.display = "none") : false
  );
});

abaGraficoPiObitos.addEventListener("click", () => {
  graficoPiObitos.style.display = "block";
  barraGraficoPiObitos.style.display = "block";

  graficosPi.map((grafico) =>
    grafico !== graficoPiObitos ? (grafico.style.display = "none") : false
  );

  barrasGraficoPi.map((barra) =>
    barra !== barraGraficoPiObitos ? (barra.style.display = "none") : false
  );
});

abaGraficoPiDoencas.addEventListener("click", () => {
  graficoPiDoencas.style.display = "block";
  barraGraficoPiDoencas.style.display = "block";

  graficosPi.map((grafico) =>
    grafico !== graficoPiDoencas ? (grafico.style.display = "none") : false
  );

  barrasGraficoPi.map((barra) =>
    barra !== barraGraficoPiDoencas ? (barra.style.display = "none") : false
  );
});

abaGraficoPiNovosCasos.addEventListener("click", () => {
  graficoPiNovosCasos.style.display = "block";
  barraGraficoPiNovosCasos.style.display = "block";

  graficosPi.map((grafico) =>
    grafico !== graficoPiNovosCasos ? (grafico.style.display = "none") : false
  );

  barrasGraficoPi.map((barra) =>
    barra !== barraGraficoPiNovosCasos ? (barra.style.display = "none") : false
  );
});

abaGraficoBrConfirmados.addEventListener("click", () => {
  graficoBrConfirmados.style.display = "block";
  barraGraficoBrConfirmados.style.display = "block";

  graficosBr.map((grafico) =>
    grafico !== graficoBrConfirmados ? (grafico.style.display = "none") : false
  );

  barrasGraficoBr.map((barra) =>
    barra !== barraGraficoBrConfirmados ? (barra.style.display = "none") : false
  );
});

abaGraficoBrObitosAcumulados.addEventListener("click", () => {
  graficoBrObitosAcumulados.style.display = "block";
  barraGraficoBrObitosAcumulados.style.display = "block";

  graficosBr.map((grafico) =>
    grafico !== graficoBrObitosAcumulados ? (grafico.style.display = "none") : false
  );

  barrasGraficoBr.map((barra) =>
    barra !== barraGraficoBrObitosAcumulados ? (barra.style.display = "none") : false
  );
});

abaGraficoBrNovosObitos.addEventListener("click", () => {
  graficoBrNovosObitos.style.display = "block";
  barraGraficoBrNovosObitos.style.display = "block";

  graficosBr.map((grafico) =>
    grafico !== graficoBrNovosObitos ? (grafico.style.display = "none") : false
  );

  barrasGraficoBr.map((barra) =>
    barra !== barraGraficoBrNovosObitos ? (barra.style.display = "none") : false
  );
});

// Menu Responsivo
let showMenu = true;

menuToggle.addEventListener("click", () => {
  document.body.style.overflow = showMenu ? "hidden" : "initial";

  secaoMenu.classList.toggle("on", showMenu);
  showMenu = !showMenu;
});
