<?php
function setFlash($tipo, $mensagem){
    $_SESSION['flash'][$tipo] = $mensagem;
}

function getFlash($tipo){
    if(isset($_SESSION['flash'][$tipo])){
        $msg = $_SESSION['flash'][$tipo];
        unset($_SESSION['flash'][$tipo]);
        return $msg;
    }
    return null;
}