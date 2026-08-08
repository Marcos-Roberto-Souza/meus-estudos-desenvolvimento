const loginBtn = document.getElementById("loginBtn");
const registerBtn = document.getElementById("registerBtn");

loginBtn.addEventListener("click", () => {
    window.location.href = "../login/index.html";
});

registerBtn.addEventListener("click", () => {
    window.location.href = "../register/index.html";
});