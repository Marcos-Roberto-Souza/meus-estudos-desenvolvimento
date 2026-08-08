<?php
require_once 'bootstrap.php';

if (!isset($_SESSION['usuario_id'])) {
    header("Location: /public/login.php");
    exit;
}


