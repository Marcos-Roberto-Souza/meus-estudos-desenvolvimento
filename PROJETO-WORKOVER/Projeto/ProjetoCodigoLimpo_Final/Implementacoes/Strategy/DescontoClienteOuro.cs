using ProjetoCodigoLimpo_Final.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ProjetoCodigoLimpo_Final.Implementacoes.Strategy
{
    public class DescontoClienteOuro : ICalculadoraDesconto
    {
        public decimal AplicarDesconto(decimal preco)
        {
            return preco - Constantes.DESCONTO_CLIENTE_OURO * preco;
        }
    }
}
