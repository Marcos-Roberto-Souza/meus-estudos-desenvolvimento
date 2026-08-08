# Sistema de Pedidos de Restaurante

## O QUE A APLICAÇÃO FAZ
Este é um sistema de gerenciamento de pedidos para restaurantes que permite:
- Cadastro e gerenciamento de produtos (cardápio)
- Cadastro de clientes
- Realização de pedidos
- Acompanhamento do status dos pedidos
- Gerenciamento administrativo

## COMO A APLICAÇÃO FUNCIONA
O sistema é dividido em duas interfaces principais:
1. **Interface do Cliente**: Onde os clientes podem:
   - Visualizar o cardápio
   - Fazer pedidos
   - Cadastrar seus dados

2. **Interface Administrativa**: Onde os administradores podem:
   - Gerenciar produtos
   - Acompanhar pedidos
   - Atualizar status dos pedidos
   - Gerenciar clientes

## FLUXO DO SISTEMA
1. **Cadastro de Cliente**
   - Cliente acessa o sistema
   - Preenche formulário de cadastro
   - Dados são salvos no banco de dados

2. **Visualização do Cardápio**
   - Cliente visualiza produtos disponíveis
   - Produtos organizados por categorias
   - Imagens e descrições dos produtos

3. **Realização de Pedido**
   - Cliente seleciona produtos
   - Adiciona ao carrinho
   - Confirma pedido

4. **Acompanhamento do Pedido**
   - Administrador visualiza pedidos
   - Atualiza status (Pendente, Preparando, Finalizado)
   - Cliente pode acompanhar status

## TECNOLOGIAS UTILIZADAS
- **Backend**: Django 5.0.2
- **Frontend**: 
  - HTML5
  - CSS3
  - Bootstrap 5
  - JavaScript
- **Banco de Dados**: SQLite
- **Gerenciamento de Imagens**: Pillow
- **Autenticação**: Django Authentication System

## COMO EXECUTAR O PROJETO
1. **Pré-requisitos**:
   - Python 3.12
   - pip (gerenciador de pacotes Python)

2. **Instalação**:
   ```bash
   # Clone o repositório
   git clone [URL_DO_REPOSITÓRIO]

   # Acesse o diretório do projeto
   cd trabalho

   # Instale as dependências
   pip install -r requirements.txt

   # Execute as migrações
   python manage.py migrate

   # Crie um superusuário
   python manage.py createsuperuser

   # Inicie o servidor
   python manage.py runserver
   ```

3. **Acesso**:
   - Interface do Cliente: http://localhost:8000/cadastro-cliente/
   - Interface Administrativa: http://localhost:8000/admin/

## AÇÕES REALIZADAS NO SISTEMA
1. **Gerenciamento de Produtos**:
   - Cadastro de produtos
   - Upload de imagens
   - Categorização
   - Controle de disponibilidade

2. **Gerenciamento de Pedidos**:
   - Criação de pedidos
   - Acompanhamento de status
   - Cálculo de valores
   - Histórico de pedidos

3. **Gerenciamento de Clientes**:
   - Cadastro de clientes
   - Armazenamento de dados
   - Histórico de pedidos

## FUNCIONALIDADES IMPLEMENTADAS
1. **Interface do Cliente**:
   - Visualização do cardápio
   - Carrinho de compras
   - Cadastro de clientes
   - Realização de pedidos

2. **Interface Administrativa**:
   - Dashboard de pedidos
   - Gerenciamento de produtos
   - Controle de status
   - Relatórios de pedidos

3. **Funcionalidades Específicas**:
   - Upload e gerenciamento de imagens
   - Formatação automática de telefone
   - Validação de formulários
   - Sistema de mensagens
   - Interface responsiva
   - Navegação intuitiva

4. **Segurança**:
   - Autenticação de usuários
   - Controle de acesso
   - Validação de dados
   - Proteção contra CSRF 