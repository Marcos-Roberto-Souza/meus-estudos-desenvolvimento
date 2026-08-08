<?php require __DIR__ . '/../layouts/header.php'; ?>

<div class="d-flex justify-content-between align-items-center mb-3">
    <h2>Usuários</h2>
    <a href="/usuarios/criar" class="btn btn-success">Novo Usuário</a>
</div>
<table class="table table-bordered table-striped">
    <thead>
        <tr>
            <th>ID</th>
            <th>Email</th>
            <th style="width: 180px;">Ações</th>
        </tr>
    </thead>
    <tbody>
        <?php if (!empty($usuarios)): ?>
            <?php foreach ($usuarios as $u): ?>
                <tr>
                    <td><?= htmlspecialchars($u['id']) ?></td>
                    <td><?= htmlspecialchars($u['email']) ?></td>
                    <td>
                        <a href="/usuarios/editar/<?= $u['id'] ?>" class="btn btn-sm btn-warning">Editar</a>
                        <a href="/usuarios/excluir/<?= $u['id'] ?>" onclick="return confirm('Deseja excluir este usuário?');" class="btn btn-sm btn-danger">Excluir</a>
                    </td>
                </tr>
                <?php endforeach; ?>
                <?php else: ?>
                    <tr>
                        <td colspan="3" class="text-center">Nenhum usuário encontrado</td>
                    </tr>
                    <?php endif; ?>
    </tbody>
</table>

<?php require __DIR__ . '/../layouts/footer.php'; ?>