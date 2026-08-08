<?php
require "conexao.php";

$id = $_GET['id'] ?? null;

if (!$id) {
    header("Location: listar.php");
    exit;
}

$sql = "SELECT * FROM usuarios WHERE id = ?";
$stmt = $pdo->prepare($sql);
$stmt->execute([$id]);
$usuario = $stmt->fetch(PDO::FETCH_ASSOC);

if (!$usuario) {
    echo "Usuário não encontrado.";
    exit;
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Editar usuário</title>
</head>
<body>

<h1>Editar usuário</h1>

<form action="atualizar.php" method="post">
    <input type="hidden" name="id" value="<?= $usuario['id'] ?>">
    <label>Nome:</label><br>
    <input type="text" name="nome"value="<?= htmlspecialchars($usuario['nome']) ?>" required>
    <br><br>
    <label>Email:</label><br>
    <input type="email" name="email" value="<?= htmlspecialchars($usuario['email']) ?>" required>
    <br><br>

    <button type="submit">Salvar alterações</button>
</form>

<br>
<a href="listar.php">Cancelar</a>

</body>
</html>