<?php

require_once __DIR__ . '/../../config/conexao.php';
require_once __DIR__ . '/../../config/helpers.php';
require_once __DIR__ . '/../Services/UsuarioService.php';
require_once __DIR__ . '/../Models/Usuario.php';

class UsuarioController
{

    private $service;
    private $model;

    public function __construct($pdo)
    {
        $this->model = new Usuario($pdo);
        $this->service = new UsuarioService($pdo);
    }

    public function index()
    {
        $usuarios = $this->service->listarUsuarios();
        require __DIR__ . '/../Views/usuarios/listar.php';
    }

    public function criar()
    {
        require __DIR__ . '/../Views/usuarios/cadastrar.php';
    }

    public function salvar()
    {
        try {
            $email = $_POST['email'] ?? '';
            $senha = $_POST['senha'] ?? '';

            if (!$email || !$senha) {
                throw new Exception('Email e senha são obrigatórios');
            }

            $this->service->cadastrarUsuario($email, $senha);

            setFlash('success', 'Usuário cadastrado com sucesso');
            header('Location: /usuarios');
            exit;

        } catch (Exception $e) {
            setFlash('error', $e->getMessage());
            header('Location: /usuarios/criar');
            exit;
        }
    }
    public function cadastrarUsuario($email, $senha)
    {
        try {
            $this->service->cadastrarUsuario($email, $senha);
            setFlash('success', 'Usuário cadastrado com sucesso');
            header('Location: /usuarios');
            exit;

        } catch (Exception $e) {
            setFlash('error', $e->getMessage());
            header('Location: /usuarios/criar');
            exit;
        }
    }

    public function salvarUsuario($email, $senha)
    {
        try {
            $this->service->cadastrarUsuario($email, $senha);
            setFlash('success', 'Usuário cadastrado com sucesso');
            header('Location: /usuarios');
            exit;

        } catch (Exception $e) {
            setFlash('error', $e->getMessage());
            header('Location: /usuarios/criar');
            exit;
        }
    }

    public function editar($id)
    {
        $usuario = $this->service->buscarUsuario($id);
        require __DIR__ . '/../Views/usuarios/editar.php';
    }

    public function atualizar()
    {
        try {
            $id = $_POST['id'] ?? null;
            $email = $_POST['email'] ?? '';

            if (!$id || !$email) {
                throw new Exception('Dados inválidos');
            }

            $this->service->atualizarUsuario($id, $email);

            setFlash('success', 'Usuário atualizado com sucesso');
            header('Location: /usuarios');
            exit;

        } catch (Exception $e) {
            setFlash('error', $e->getMessage());
            header('Location: /usuarios');
            exit;
        }
    }


    public function excluir($id)
    {
        if (!$id) {
            header('Location: /usuarios');
            exit;
        }

        $this->model->excluir($id);

        header('Location: /usuarios');
        exit;
    }


}