using ProjetoCodigoSujo_4SOLIDPadroes.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCodigoSujo_4SOLIDPadroes.Implementacoes.Strategy
{
    public class DescontoClientePadrao : ICalculadoraDesconto
    {
        public decimal AplicarDesconto(decimal preco)
        {
            // Cliente padrão não recebe desconto
            return preco;
        }

    }
}
