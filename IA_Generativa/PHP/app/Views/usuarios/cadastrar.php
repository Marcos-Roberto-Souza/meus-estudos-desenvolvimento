<?php

require __DIR__ . '/../layouts/header.php'; ?>

<h2>Novo Usuário</h2>

<form method="POST" action="/usuarios/salvar">
    <div>
        <label>Email</label>
        <input type="email" name="email" required>
    </div>
    <br><br>
    <div>
        <label>Senha</label>
        <input type="password" name="senha" required>
    </div>
    <br><br>
    <button type="submit">Salvar</button>
</form>

<?php require __DIR__ . '/../layouts/footer.php'; ?>
