const form = document.getElementById("loginForm");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const errorMessage = document.getElementById("error");
const loginBtn = document.getElementById("loginBtn");

if (!errorMessage) {
    console.error("Elemento #error não encontrado no HTML");
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    errorMessage.textContent = "";

    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();

    const users = JSON.parse(localStorage.getItem("users")) || [];

    const user = users.find(
        u => u.email === email && u.password === password
    );

    if (!user) {
        errorMessage.textContent = "E-mail ou senha incorretos.";
        return;
    }

    localStorage.setItem("loggedUser", JSON.stringify(user));
    window.location.href = "../dashboard/index.html";


});