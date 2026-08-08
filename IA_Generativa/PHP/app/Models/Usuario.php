<?php

class Usuario{

    private $pdo;

    public function __construct($pdo){
        $this->pdo = $pdo;
    }

    public function listar(){
        $sql = "SELECT id, email FROM usuarios";
        return $this->pdo->query($sql)->fetchAll();
    }

    public function cadastrar($email, $senha){
        $sql = "INSERT INTO  usuarios (email, senha) VALUES (?, ?)";
        $stmt = $this->pdo->prepare($sql);
        return $stmt->execute([$email, $senha]);
    }

    public function atualizar($id, $email){
        $sql = "UPDATE usuarios SET email = ? WHERE id = ?";
        $stmt = $this->pdo->prepare($sql);
        return $stmt->execute([$email, $id]);
    }

    public function excluir($id){
        $sql = "DELETE FROM usuarios WHERE id = ?";
        $stmt = $this->pdo->prepare($sql);
        return $stmt->execute([$id]);
    }

    public function buscarPorEmail($email){
        $sql = "SELECT * FROM usuarios WHERE email = ?";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute([$email]);
        return $stmt->fetch();
    }

    public function buscarPorId($id){
        $sql = "SELECT * FROM usuarios WHERE id = ?";
        $stmt = $this->pdo->prepare($sql);
        $stmt->execute([$id]);
        return $stmt->fetch();
    }
}