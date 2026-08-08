<?php
require_once __DIR__ . '/../config/bootstrap.php';
require_once __DIR__ . '/../config/conexao.php';
require_once __DIR__ . '/../app/Controllers/UsuarioController.php';

$uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
$uri = trim($uri, '/');
$partes = explode('/', $uri);

$controller = $partes[0] ?? 'usuarios';
$acao       = $partes[1] ?? 'index';
$id         = $partes[2] ?? null;

// Corrige quando vier "public"
if ($controller === 'public') {
    $controller = $partes[1] ?? 'usuarios';
    $acao       = $partes[2] ?? 'index';
    $id         = $partes[3] ?? null;
}

switch ($controller) {
    case 'usuarios':
        $c = new UsuarioController($pdo);

        switch ($acao) {
            case 'criar':
                $c->criar();
                break;

            case 'editar':
                $c->editar($id);
                break;

            case 'atualizar':
                $c->atualizar();
                break;
            
            case 'salvar':
                $c->salvar();
                break;
            
            case 'excluir':
                $c->excluir($id);
                break;
            
            case 'login':
                require __DIR__ . '/login.php';
                break;

            case 'login_processa':
                require __DIR__ . '/login_processa.php';
                break;
            
            case 'logout':
                require __DIR__ . '/logout.php';
                break;

            default:
                $c->index();
                break;
        }
        break;

    default:
        echo 'Rota não encontrada';
}