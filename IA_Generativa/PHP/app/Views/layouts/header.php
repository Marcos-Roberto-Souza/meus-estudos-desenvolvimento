<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>Sistema</title>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap -->

</head>

<body>

    <nav class="navbar navbar-dark bg-dark mb-4">
        <div class="container">

            <?php if ($msg = getFlash('success')): ?>
                <div class="alert alert-success"><?= $msg ?></div>
            <?php endif; ?>

            <?php if ($msg = getFlash('error')): ?>
                <div class="alert alert-danger"><?= $msg ?></div>
            <?php endif; ?>

            <span class="navbar-brand">Meu Sistema</span>
            <a href="/logout" class="btn btn-outline-light btn-sm">Sair</a>
        </div>
    </nav>

    <div class="container"></div>