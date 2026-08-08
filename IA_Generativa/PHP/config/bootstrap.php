<?php

if (session_status() === PHP_SESSION_NONE){
    session_start();
}

require_once __DIR__ . '/env.php';
require_once __DIR__ . '/error_handler.php';
require_once __DIR__ . '/helpers.php';
require_once __DIR__ . '/flash.php';
require_once __DIR__ . '/permissions.php';

date_default_timezone_set('America/Sao_Paulo');