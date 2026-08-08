package problemas;

//Leia um valor de ponto flutuante com duas casas decimais. 
//Este valor representa um valor monetário. A seguir, 
//calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
//As notas consideradas são de 100, 50, 20, 10, 5, 2. 
//As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
//A seguir mostre a relação de notas necessárias.
//
//Entrada
//O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
//
//Saída
//Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
//
//Obs: Utilize ponto (.) para separar a parte decimal.

import java.util.*;

public class Problema1021 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		float dinheiro = teclado.nextFloat();
		
		int centavos = (int)Math.round(dinheiro * 100);
		
		String[] notasNomes = {
				"R$ 100.00",
				"R$ 50.00",
				"R$ 20.00",
				"R$ 10.00",
				"R$ 5.00",
				"R$ 2.00"
		};
		
		int[] notasValores = {
				10000,
				5000,
				2000,
				1000,
				500,
				200
		};
		
		String[] moedasNomes = {
				"R$ 1.00",
				"R$ 0.50",
				"R$ 0.25",
				"R$ 0.10",
				"R$ 0.05",
				"R$ 0.01"
		};
		
		int[] moedasValores = {
				100,
				50,
				25,
				10,
				5,
				1
		};
		
		System.out.println("NOTAS:");
		
		for (int i = 0; i<notasValores.length; i++) {
			int quantidade = centavos / notasValores[i];
			centavos %=notasValores[i];
			
			System.out.println(quantidade + " nota(s) de " + notasNomes[i]);
			
		}
		
		System.out.println("MOEDAS:");
		
		for (int i = 0; i<moedasValores.length; i++) {
			int quantidade = centavos / moedasValores[i];
			centavos %=moedasValores[i];
			
			System.out.println(quantidade + " moeda(s) de " + moedasNomes[i]);
			
		}
		
		teclado.close();

	}

}
