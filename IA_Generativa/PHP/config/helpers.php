<?php

function limpar($valor){
    return htmlspecialchars(trim($valor), ENT_QUOTES, 'UTF-8');
}