<?php
require "conexao.php";

$id    = $_POST['id'] ?? null;
$nome  = $_POST['nome'] ?? null;
$email = $_POST['email'] ?? null;

if (!$id || !$nome || !$email) {
    echo "Dados inválidos.";
    exit;
}

$sql = "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?";
$stmt = $pdo->prepare($sql);
$stmt->execute([$nome, $email, $id]);

header("Location: listar.php");
exit;