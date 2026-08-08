const welcome = document.getElementById("welcome");
const logoutBtn = document.getElementById("logout");

const loggedUser = JSON.parse(localStorage.getItem("loggedUser"));

if (!loggedUser) {
    // ✅ Bloqueia acesso direto
    window.location.href = "../login/index.html";
} else {
    welcome.textContent = `Bem-vindo, ${loggedUser.name}!`;
}

logoutBtn.addEventListener("click", () => {
    localStorage.removeItem("loggedUser");
    window.location.href = "../login/index.html";
});

function abrirProjeto2026() {
    window.location.href = "../gerador-CSS/index.html";
}



