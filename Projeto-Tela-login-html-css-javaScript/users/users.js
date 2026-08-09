const userList = document.getElementById("userList");

function loadUsers() {
    const users = JSON.parse(localStorage.getItem("users")) || [];

    if (users.length === 0) {
        userList.innerHTML = "<li>Nenhum usuário cadastrado.</li>";
        return;
    }

    userList.innerHTML = "";

    users.forEach((user, index) => {
        const li = document.createElement("li");

        li.innerHTML = `
        <strong>${user.name}</strong><br>
        <span>${user.email}</span>
        `;

        userList.appendChild(li);
    });
}

loadUsers();
