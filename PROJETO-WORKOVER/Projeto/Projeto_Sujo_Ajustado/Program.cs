//Clean Code é o código autoexplicativo, onde cada
//linha revela seu propósito sem a necesidade de cometários excessivos.

//Chega de códigos obscuros e redundantes. Clean Code traz clareza e eficiência!.

// "Indentificadores"
//Um identificador é um nome atribuído a um tipo (classe, interface, struct, record, delegate, enum), membro, propriedade,variável ou namespace.

//Regras gerais para identificadores válidos em C#:
// Devem começar com uma letra ou sublinhado (_).
// Não podem iniciar com um número ou caractere especial: #, @, $, etc.
// Não podem conter espaços ou caracteres especiais.


// Convenções usadas para identificadores com mais de uma palavra:
// CamelCase: A primeira letra de cada palavra é minuúscula. Exemplo: minhaVariavel, minhaFuncao().

// PascalCase: A primeira letra de cada palavra é maiúscula. Exemplo: MinhaClasse, MinhaPropriedade.
// Usado em nome de classes, interfaces, métodos e propriedades.

// Convenções para Constantes:
// Usar todas as letras maiúsculas separando com sublinhado (_).
// Ex: PI, VALOR_DESCONTO, IMPOSTO_ESTADUAL.
// Sublinhado (_)
// Usado no início do nome para campos internos privados e somente leitura (Segue CamelCase).
// Ex: _minhaVariavel, _minhaPropriedade, _minhaConstante.

// "Classes" : Substantivos descritivos em PascalCase, representando o que a classe é ou faz.
// "Métodos" : Verbos descritivos em PascalCase, revelando a ação do método.
// "Variáveis" : Substantivos descritivos em CamelCase, indicando o que a variável armazena.
// "Parâmetros" : Substantivos descritivos em CamelCase, representando o papel do parâmetro.
// "Constantes" : Substantivos descritivos em CaixaAlta, com palavras separadas por sublinhado.

// Os números mágicos são valores literais(inteiros, decimais, strings) espalhados pelo código sem um significado claro ou contexto explicativo
// que dificultam a leitura, manutenção e compreensão do código.
//
// * Legibilidade comprometida
// * Códigos inconsistentes
// * Suscetibilidade a erros
// * Impacto negativo na qualidade do código

//Combatendo os números mágicos com Clean Code:
// Usar constantes nomeadas

//Criar constantes com nomes descritivos para representar os valores mágicos
// Exemplo:
// DESCONTO_STATUS_ATIVO = 0.1m;
// DESCONTO_PROMOCIONAL = 0.7m;
// DESCONTO_VIP = 0.5m;
// DESCONTO_MAXIMO_POR_FIDELIDADE = 5;

// Agrupar constantes em enumerações (enums)
// Se houver diversos valores mágicos relacionados a um mesmo contexto, agrupe-os em enums para melhor organização e legibilidade.
// Exemplo:
//public enum StatusDaConta
//{
//    ClientePadrao = 1,
//    ClienteEspecial,
//    ClienteOuro,
//    ClienteVIP
//
//}
//Criar funções e/ou métodos para cálculos
// Encapsular cálculos complexos que envolvam números mágicos em funções/métodos com nomes descritivos para facilitar a reutilização de código.
//Exemplo:
// CalcularPrecoComDesconto(precoProduto, desconto, percentualDescontoFidelidade);

// Centralize as constantes em um único lugar
// Centralizar suas constantes eu um único arquivo ou classe, especialmente se forem usadas em várias partes do projeto.
// Exemplo:
//public static class Constantes
//{
//    public const int DESCONTO_MAXIMO_POR_FIDELIDADE = 5;
//    public const decimal DESCONTO_CLIENTE_ESPECIAL = 0.1m;
//    public const decimal DESCONTO_CLIENTE_OURO = 0.3m;
//    public const decimal DESCONTO_CLIENTE_VIP = 0.5m;
//}
//
// const cria uma variável imutável com um valor definido no momento da declaração.
//

namespace Projeto;

public class CalculadoraDeDesconto
{
    public decimal CalcularDesconto(decimal precoDoProduto,
                                    int statusDaConta,
                                    int tempoDeContaEmAnos)
    {
        decimal precoDepoisDoDesconto = 0;
        decimal percentualDoDescontoPorFidelidade = (tempoDeContaEmAnos > 5) ?
                                                    (decimal)5 / 100 :
                                                    (decimal)tempoDeContaEmAnos / 100;

        if (statusDaConta == 1)
        {
            precoDepoisDoDesconto = precoDoProduto;
        }
        else if (statusDaConta == 2)
        {
            precoDepoisDoDesconto = CalcularPrecoDepoisDoDesconto(precoDoProduto, 0.1m, percentualDoDescontoPorFidelidade);
                                    
        }
        else if (statusDaConta == 3)
        {
            precoDepoisDoDesconto = CalcularPrecoDepoisDoDesconto(precoDoProduto, 0.3m, percentualDoDescontoPorFidelidade);
        }
        else if (statusDaConta == 4)
        {
            precoDepoisDoDesconto = CalcularPrecoDepoisDoDesconto(precoDoProduto, 0.5m, percentualDoDescontoPorFidelidade);
        }
        return precoDepoisDoDesconto;

    }

    public decimal CalcularPrecoDepoisDoDesconto(decimal precoDoProduto, 
                                                decimal percentualDesconto, 
                                                decimal percentualDoDescontoPorFidelidade)
    {
        decimal precoComDesconto = precoDoProduto - (percentualDesconto * precoDoProduto);
        return precoComDesconto - (percentualDoDescontoPorFidelidade * precoComDesconto);
    }
}






