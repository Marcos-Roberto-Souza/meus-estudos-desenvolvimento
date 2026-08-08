<?php

require_once __DIR__ . '/env.php';

ini_set('display_errors', SHOW_ERRORS ? '1' : '0');
ini_set('log_errors', '1');
ini_set('error_log', __DIR__ . '/../logs/app.log');

error_reporting(E_ALL);

set_exception_handler(function ($exception) {

    $mensagem = sprintf(
        "[%s] %s em %s:%d\nStack: %s\n\n",
        date('Y-m-d H:i:s'),
        $exception->getMessage(),
        $exception->getFile(),
        $exception->getLine(),
        $exception->getTraceAsString()
    );

    error_log($mensagem);

    if (SHOW_ERRORS) {
        echo "<pre>{$mensagem}</pre>";
    } else {
        header("Location: /500");
        exit;
    }
});