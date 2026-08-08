using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCodigoSujo_4SOLIDPadroes.Interfaces
{
    public interface ICalculadoraDeDescontoPorFidelidade
    {
        decimal CalcularDesconto(decimal precoProduto, int tempoDaContaEmAnos);
    }
}
