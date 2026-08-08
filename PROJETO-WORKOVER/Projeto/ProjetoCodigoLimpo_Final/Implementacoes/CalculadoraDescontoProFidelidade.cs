using ProjetoCodigoLimpo_Final.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCodigoLimpo_Final.Implementacoes
{
    public class CalculadoraDescontoProFidelidade : ICalculadoraDeDescontoPorFidelidade
    {
        public decimal CalcularDesconto(decimal precoProduto, int tempoDaContaEmAnos)
        {
            decimal percentualDescontoPorFidelidade =
                tempoDaContaEmAnos > Constantes.DESCONTO_MAXIMO_POR_FIDELIDADE ?
                Constantes.DESCONTO_MAXIMO_POR_FIDELIDADE / 100 :
                (decimal)tempoDaContaEmAnos / 100;

            var precoComDesconto = precoProduto - percentualDescontoPorFidelidade * precoProduto;

            return precoComDesconto;
        }
    }
}
