<?php

function isAdmin() {
    return isset($_SESSION['usuario_role']) && $_SESSION['usuario_role'] === 'admin';
}

function authorizeAdmin() {
    if (!isAdmin()) {
        setFlash('error', 'Acesso não autorizado');
        header('Location: /dashboard');
        exit;
    }
}