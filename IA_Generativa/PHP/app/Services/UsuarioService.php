<?php

require_once __DIR__ . '/../Models/Usuario.php';

class UsuarioService {

    private $usuarioModel;

    public function __construct($pdo) {
        $this->usuarioModel = new Usuario($pdo);
    }

    public function cadastrarUsuario($email, $senha) {

        if (empty($email) || empty($senha)) {
            throw new Exception("Email e senha são obrigatórios");
        }

        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Email inválido");
        }

        if (strlen($senha) < 6) {
            throw new Exception("Senha deve ter no mínimo 6 caracteres");
        }

        $existe = $this->usuarioModel->buscarPorEmail($email);
        if ($existe) {
            throw new Exception("Este email já está cadastrado");
        }

        $senhaHash = password_hash($senha, PASSWORD_DEFAULT);

        return $this->usuarioModel->cadastrar($email, $senhaHash);
    }

    public function atualizarUsuario($id, $email) {

        if (empty($id) || empty($email)) {
            throw new Exception("Dados inválidos");
        }

        return $this->usuarioModel->atualizar($id, $email);
    }

    public function excluirUsuario($id) {

        if ($id == $_SESSION['usuario_id']) {
            throw new Exception("Você não pode excluir seu próprio usuário");
        }

        return $this->usuarioModel->excluir($id);
    }

    public function listarUsuarios() {
        return $this->usuarioModel->listar();
    }

    public function buscarUsuario($id) {
        return $this->usuarioModel->buscarPorId($id);
    }
}