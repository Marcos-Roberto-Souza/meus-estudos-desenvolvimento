package problemas;

//Leia 3 valores inteiros e ordene-os em ordem crescente. 
//No final, mostre os valores em ordem crescente, 
//uma linha em branco e em seguida, 
//os valores na sequência como foram lidos.
//
//Entrada
//A entrada contem três números inteiros.
//
//Saída
//Imprima a saída conforme foi especificado.
//
//Exemplo de Entrada
//
//7 21 -14
//
//
//Exemplo de Saída
//
//-14
//7
//21
//
//7
//21
//-14

import java.util.*;

public class Problema1042 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int valorA = teclado.nextInt();
		int valorB = teclado.nextInt();
		int valorC = teclado.nextInt();
		
		int[] valores = {valorA, valorB, valorC};
		
		Arrays.sort(valores);
		
		for(int v : valores) {
			System.out.println(v);
		}
		
		System.out.println();
		System.out.println(valorA);
		System.out.println(valorB);
		System.out.println(valorC);
		
		teclado.close();

	}

}
