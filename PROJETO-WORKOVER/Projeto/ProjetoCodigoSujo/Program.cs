// Passo 1
// Atacando o problema da nomeclatura usada no código sujo,

// Antes     |       Depois
//___________|_______________________________
// calc1     |    CalculadoraDeDesconto
// calculos  |    CalcularDesconto
// val       |    precoDoProduto
// tip       |    statusDaConta
// anos      |    tempoDeContaEmAnos
// res       |    precoDepoisDoDesconto
// desc      |    percentualDoDescontoPorFidelidade

//Depois do ajuste aplicado agora da para entender que 
// A classe CalculadoraDeDesconto vai usar o método CalcularDesconto para calcular o preço de um produto
// após aplicar um desconto baseado no status da conta e no tempo de fidelidade da conta.
// Aplicado método clean Code, aplicando a nomeclatura.
//
//Passo 2
//identificar os números ou valores mágicos e atacar o problema dos números mágicos,
// Examinando o código em busca de valores literais que não estejam associados a variáveis explicativas ou constantes nomeadas e
// por padrões de números repetidos que  podem indicar valores mágicos ocultos.
namespace Projeto;

public class  calc1
{
    public decimal calculos(decimal val, 
                            int tip, 
                            int anos) 
    {
        decimal res = 0;
        decimal desc = (anos > 5) ? 
                       (decimal)5 / 100 : 
                       (decimal)anos / 100;

        if(tip == 1) 
        { 
            res = val; 
        } 
        else if(tip == 2) 
        { 
            res = (val - (0.1m * val)) 
                - desc * (val - (0.1m * val)); 
        }
        else if(tip == 3) 
        { 
            res = (0.7m * val) 
                - desc * (0.7m * val);
        }
        else if(tip == 4) 
        { 
            res = (val - (0.5m * val)) 
                - desc * (val - (0.5m * val)); 
        }
            return res;
    }
}
// codigo sujo, sem organização, sem boas práticas, sem padrões de projeto, sem SOLID, sem DRY, sem KISS, sem YAGNI,
// sem princípios de design, sem princípios de desenvolvimento,
// sem princípios de programação, sem princípios de engenharia de software,
// sem princípios de arquitetura de software, sem princípios de design de software,
// sem princípios de desenvolvimento de software, sem princípios de programação orientada a objetos,
// sem princípios de programação funcional, sem princípios de programação estruturada, sem princípios de programação procedural,
// sem princípios de programação orientada a aspectos, sem princípios de programação orientada a eventos,
// sem princípios de programação orientada a dados, sem princípios de programação orientada a objetos e aspectos,
// sem princípios de programação orientada a objetos e eventos, sem princípios de programação orientada a objetos e dados,
// sem princípios de programação orientada a aspectos e eventos, sem princípios de programação orientada a aspectos e dados,
// sem princípios de programação orientada a eventos e dados.
// A formatação e identação do código dificulta a leitura e compreensão do código, tornando-o difícil de entender.
// Classe viola o principio do SRP, pois tem mais de uma responsabilidade, além de não seguir o principio do OCP, pois não é aberta para extensão e fechada para modificação.
