
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Teste PHP</title>
</head>
<body>

<h1>Olá!</h1>

<form action="aprendendo.php" method="post">
    <label for="nome">Nome:</label>
    <input type="text" id="nome" name="nome"><br><br>

    <label for="ano_atual">Ano Atual:</label>
    <input type="number" id="ano_atual" name="ano_atual"><br><br>

    <label for="ano_nascimento">Ano de Nascimento:</label>
    <input type="number" id="ano_nascimento" name="ano_nascimento"><br><br>

    <input type="submit" value="Enviar">

<?php
$nome = $_POST['nome'];
$ano_atual = $_POST['ano_atual'];
$ano_nascimento = $_POST['ano_nascimento'];
$idade = $ano_atual - $ano_nascimento;


echo "<p>Bem-vindo, $nome <br> Você tem $idade anos.</p>";
?>

</body>
</html>
