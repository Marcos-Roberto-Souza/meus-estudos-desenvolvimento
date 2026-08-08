<?php
session_start();

if (!isset($_SESSION['usuario_id'])) {
    header("Location: login.php");
    exit;
}
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Painel</title>
</head>
<body>

<h1>Bem-vindo, <?= htmlspecialchars($_SESSION['usuario_nome']) ?></h1>

<p>Você está logado.</p>

logout.phpSair</a>

</body>
</html>