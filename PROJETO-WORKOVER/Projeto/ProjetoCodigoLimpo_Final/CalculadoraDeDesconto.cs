// Os princípios SOLID e os padrões de projeto garantem um código limpo e fácil de ajustar.
// Principios SOLID:
// São um conjunto de cinco princípios de design de software qeu visam tornar o código mais compreensível, flexível e fácil de manter.
// Eles foram introduzidos por Robert C. Martin, também conhecido como " Uncle Bob ".
//Cada letra em SOLID representa um princípio específico:
// SRP, OCP, LSP, ISP , DIP.

// SRP (Single Responsibility Principle): O princípio da responsabilidade única (SRP) diz que uma classe deve ter apenas uma tarefa ou responsabilidade.
// Uma classe deve ter apenas um motivo para ser alterada, ou seja, deve ser implementada tendo apenas um único objetivo.
// Ter responsabilidades bem definidas torna o código mais organizado e facilita a conexão entre diferentes partes do sistema,
// ajudando a evitar problemas quando você precisa mudar alguma coisa e tornando isso mais simples e seguro.

// OCP (Open-Closed Principle):
// O princípio aberto-fechado (OCP) afirma que o código deve ser aberto para extensão, mas fechado para modificação.
// Isso significa qeu você deve poder adicionar novas funcionalidades sem alterar o código existente, evitando assim o risco de introduzir
// novos erros ou modificar o que já está funcionando.
// Como?
// Usar interfaces e abstrações
// Padrão Decorator
// Padrão Strategy
// Injeção de dependência

// LSP (Liskov Substitution Principle):
// O princípio de substituição de Liskov (LSP) afirma que objetos de uma classe derivada devem poder substituir objetos da classe base
// sem alterar o comportamento correto do programa.
// Em outras palavras, as subclasses devem ser substituíveis pelas suas superclasses sem causar erros ou comportamentos inesperados.
// Isso garante que as subclasses estendem a funcionalidade da classe base de forma que mantenha a integridade  e o contrato definido pela classe base.

// ISP (Interface Segregation Principle):
// O princípio da segregação de interfaces (ISP) afirma que uma classe não deve ser forçada a implementar interfaces que ela não usa.
// Em vez disso, deve-se criar interfaces pequenas e específicas que sejam usadas apenas pelas classes que realmente precisam delas.
// Isso ajuda a manter o código mais limpo e evita que classes sejam sobrecarregadas com métodos que não são relevantes para elas.
// Muitas interfaces específicas são melhores do que uma interface geral.

// DIP (Dependency Inversion Principle):
// O princípio da inversão de dependência (DIP) diz que as classes de alto nível não devem depender de classes de baixo nível, mas sim de abstrações(interfaces ou classes abstratas).
// Além disso, as abstrações não devem depender de detalhes, mas os detalhes devem depender das abstrações.
// Isso ajuda a manter o código mais flexível e facilita mudanças, porque você pode ajustar as partes menores sem afetar o todo.

// Padrões de projeto:
// Os padrões de projetos (design patterns) são soluções reutilizáveis para problemas comuns que ocorrem no desenvolvimento de software.
// Eles são baseados em experiências e práticas estabelecidas no campo da engenharia de software.
// Temos diversos padrões de projeto e talvez os mais famosos sejam os padrões GoF (Gang of Four).
// Vamos aplicar 2 desses padrões de projeto:
// Padrão Factory e Strategy Aplicados.
// Agora vamos aplicar a dependência DIP.




using ProjetoCodigoLimpo_Final.Interfaces;

namespace ProjetoCodigoLimpo_Final;

public class CalculadoraDeDesconto
{
    private readonly ICalculadoraDescontoStatusContaFactory _calculadoraDescontoStatusContaFactory;
    private readonly ICalculadoraDeDescontoPorFidelidade _calculadoraDescontoPorFidelidade;

    public CalculadoraDeDesconto(ICalculadoraDescontoStatusContaFactory calculadoraDescontoStatusContaFactory,
                                ICalculadoraDeDescontoPorFidelidade calculadoraDescontoPorFidelidade)
    {
         _calculadoraDescontoStatusContaFactory = calculadoraDescontoStatusContaFactory;
         _calculadoraDescontoPorFidelidade = calculadoraDescontoPorFidelidade;
    }

    public decimal AplicarDesconto(decimal precoDoProduto, StatusDaConta statusDaConta, int tempoDaContaEmAnos)
    {
        var calculadoraDesconto = _calculadoraDescontoStatusContaFactory.GetCalculadoraDescontoStatusConta(statusDaConta);
        var precoComDescontoStatusConta = calculadoraDesconto.AplicarDesconto(precoDoProduto);
        var precoFinal = _calculadoraDescontoPorFidelidade.CalcularDesconto(precoComDescontoStatusConta, tempoDaContaEmAnos);
        return precoFinal;
    }
}