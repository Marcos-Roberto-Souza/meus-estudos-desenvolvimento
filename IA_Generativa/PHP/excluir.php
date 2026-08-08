<?php
require "conexao.php";

$id = $_GET['id'];

$sql = "DELETE FROM usuarios WHERE id = ?";
$stmt = $pdo->prepare($sql);
$stmt->execute([$id]);


if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    die('Acesso inválido');
}



header("Location: listar.php");
exit;