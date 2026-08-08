<h2>LOGIN</h2>

<?PHP if (isset($_GET['erro'])): ?>
    <p style="color:red;"> Email ou Senha inválidos</p>
    <?php endif; ?>

    <form method="POST" action="/login_processa">
        <label>Email</label>
        <input type="email" name="email" required><br><br>

        <label>Senha</label><br>
        <input type="password" name="senha" required><br><br>

        <button type="submit">Entrar</button>
    </form>