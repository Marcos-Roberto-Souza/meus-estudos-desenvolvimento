package problemas;

//Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.
//
//Entrada
//Seis valores, negativos e/ou positivos.
//
//Saída
//Imprima uma mensagem dizendo quantos valores positivos foram lidos.


import java.util.*;

public class Problema1060 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
						
		int count = 0;
		
		for(int n = 0; n < 6;n++) {
			float num = teclado.nextFloat();
			if (num >= 0) 
			{
				count++;
			}
		}		
		System.out.println(count + " valores positivos");
		teclado.close();

	}

}