using ProjetoCodigoSujo_4SOLIDPadroes.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCodigoSujo_4SOLIDPadroes.Implementacoes.Strategy
{
    public class DescontoClienteEspecial : ICalculadoraDesconto
    {
        public decimal AplicarDesconto(decimal preco)
        {
            return preco - (Constantes.DESCONTO_CLIENTE_ESPECIAL * preco);
        }
    }
}
