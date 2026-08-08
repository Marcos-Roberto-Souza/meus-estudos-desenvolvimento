const form = document.getElementById("registerForm");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirmPassword");
const errorMessage = document.getElementById("error");
const registerBtn = document.getElementById("registerBtn");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = nameInput.value.trim();
    const email = emailInput.value.trim();
    const password = passwordInput.value.trim();
    const confirmPassword = confirmPasswordInput.value.trim();

    clearError();

    if (name.length < 3) {
        showError("Informe seu nome completo.");
        return;
    }

    if (!validateEmail(email)) {
        showError("E-mail inválido.");
        return;
    }

    if (password.length < 6) {
        showError("Senha deve ter no mínimo 6 caracteres.");
        return;
    }

    if (password !== confirmPassword) {
        showError("As senhas não coincidem.");
        return;
    }

    fakeRegister();
});

function validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function showError(message) {
    errorMessage.textContent = message;
}

function clearError() {
    errorMessage.textContent = "";
}


function fakeRegister() {
    const users = getUsers();

    const newUser = {
        name: nameInput.value.trim(),
        email: emailInput.value.trim(),
        password: passwordInput.value.trim()
    };

    // Verificar se o e-mail já existe
    const userExists = users.some(user => user.email === newUser.email);

    if (userExists) {
        showError("Este e-mail já está cadastrado.");
        return;
    }

    registerBtn.disabled = true;
    registerBtn.textContent = "Cadastrando...";

    setTimeout(() => {
        users.push(newUser);
        saveUsers(users);

        alert("Conta criada com sucesso!");
        window.location.href = "../login/index.html";
    }, 1000);

}

function getUsers() {
    return JSON.parse(localStorage.getItem("users")) || [];
}

function saveUsers(users) {
    localStorage.setItem("users", JSON.stringify(users));
}
