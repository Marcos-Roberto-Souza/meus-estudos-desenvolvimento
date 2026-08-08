package problemas;

//Entrada
//O arquivo de entrada contém dois valores inteiros correspondentes ao código e à 
//quantidade de um item conforme tabela acima.
//
//Saída
//O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, 
//com 2 casas após o ponto decimal.

import java.util.*;

public class Problema1038 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Map<Integer, Double> produto = new HashMap<>();
		
		produto.put(1, 4.00);
		produto.put(2, 4.50);
		produto.put(3, 5.00);
		produto.put(4, 2.00);
		produto.put(5, 1.50);
		
		Scanner teclado = new Scanner(System.in);
		
		int codigoProduto = teclado.nextInt();
		int quantidadeProduto = teclado.nextInt();
		
		double valorProduto = produto.get(codigoProduto);		
		double totalConta = valorProduto * quantidadeProduto;
		
		System.out.printf("Total: R$ %.2f%n", totalConta);
		
		teclado.close();
		

	}

}
