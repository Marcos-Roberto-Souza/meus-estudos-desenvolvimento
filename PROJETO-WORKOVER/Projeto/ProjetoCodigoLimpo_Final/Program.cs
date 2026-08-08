//Usando a classe CalculadoraDeDesconto,
//configurar a resolução das dependências na classe Program (método Main) - Princípio DIP
// Pacote Nuget: Microsoft.Extensions.DependencyInjection.
// Melhorias aplicadas ao código:

// 1 - Criação das interfaces e uso da injeção de dependência
// 2 - Responsabilidade única
// 3 - Utilização de Nomes Descritivos
// 4 - Uso de constantes
// 5 - Uso de enumeração
// 6 - Implementamos padrões de projetos: Strategy e Factory
// 7 - Melhoramos a testabilidade do código

// Princípios do Clean Code aplicados:
// 1 - Nomes Descritivos
// 2 - Responsabilidade Única
// 3 - DRY (Don't Repeat Yourself)
// 4 - KISS (Keep It Simple, Stupid)
// 5 - Encapsulamento
// 6 - Uso de constantes e enumerações
// 7 - Testabilidade : Princípio SRP e princípio Separation of Concerns


using Microsoft.Extensions.DependencyInjection;
using ProjetoCodigoLimpo_Final;
using ProjetoCodigoLimpo_Final.Interfaces;
using ProjetoCodigoLimpo_Final.Implementacoes.Factory;
using ProjetoCodigoLimpo_Final.Implementacoes;


var serviceProvider = new ServiceCollection()
    .AddScoped<ICalculadoraDescontoStatusContaFactory, CalculadoraDescontoStatusContaFactory>()
    .AddScoped<ICalculadoraDeDescontoPorFidelidade, CalculadoraDescontoProFidelidade>()
    .AddScoped<CalculadoraDeDesconto>()
    .BuildServiceProvider();

var calculadoraDeDesconto = serviceProvider.GetService<CalculadoraDeDesconto>() 
    ?? throw new InvalidOperationException("A instância de CalculadoraDeDesconto não pôde ser criada. ");

decimal precoDoProduto = 100m;
int tempoDaContaEmAnos = 3;

decimal precoComDesconto  = calculadoraDeDesconto.AplicarDesconto(precoDoProduto, 
                                                                StatusDaConta.ClientePadrao, tempoDaContaEmAnos);

Console.WriteLine($"\nCliente Padrao - Preco com Desconto: {precoComDesconto: C}");

precoComDesconto = calculadoraDeDesconto.AplicarDesconto(precoDoProduto, 
                                                                StatusDaConta.ClienteEspecial, tempoDaContaEmAnos);
Console.WriteLine($"\nCliente Especial - Preco com Desconto: {precoComDesconto: C}");

precoComDesconto = calculadoraDeDesconto.AplicarDesconto(precoDoProduto,
                                                                StatusDaConta.ClienteOuro, tempoDaContaEmAnos);
Console.WriteLine($"\nCliente Ouro - Preco com Desconto: {precoComDesconto: C}");

precoComDesconto = calculadoraDeDesconto.AplicarDesconto(precoDoProduto,
                                                                StatusDaConta.ClienteVIP, tempoDaContaEmAnos);
Console.WriteLine($"\nCliente VIP - Preco com Desconto: {precoComDesconto: C}");

Console.ReadKey();

