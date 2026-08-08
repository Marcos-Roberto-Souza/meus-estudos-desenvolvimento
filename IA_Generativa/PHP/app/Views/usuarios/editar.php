<?php

require __DIR__ . '/../layouts/header.php'; ?>

<h2>Editar Usuário</h2>

<form method="POST" action="/usuarios/atualizar">
    <input type="hidden" name="id" value="<?=$usuario['id'] ?>">

    <div>
        <label>Email</label>
        <input type="email" name="email" value="<?=  htmlspecialchars($usuario['email']) ?>"required>
    
    </div>
    <br><br>
    <button type"submit">Salvar</button>
</form>

<?php require __DIR__ . '/../layouts/footer.php'; ?>