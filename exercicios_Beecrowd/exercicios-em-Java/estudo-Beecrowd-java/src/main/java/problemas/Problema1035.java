package problemas;

//Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".
//
//Entrada
//Quatro números inteiros A, B, C e D.
//
//Saída
//Mostre a respectiva mensagem após a validação dos valores.
//
//Exemplo de Entrada			|Exemplo de Saída
//							|
//5 6 7 8						|Valores nao aceitos
//-------------------------------------------------							|
//2 3 2 6						|Valores aceitos

import java.util.*;

public class Problema1035 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner teclado = new Scanner(System.in);
		
		int valorA = teclado.nextInt();
		int valorB = teclado.nextInt();
		int valorC = teclado.nextInt();
		int valorD = teclado.nextInt();
		
		if (valorB > valorC &&
			valorD > valorA && 
			valorC + valorD > valorA + valorB && 
			valorC > 0 && valorD > 0 && 
			valorA%2==0){
			System.out.println("Valores aceitos");
		}else {
			System.out.println("Valores nao aceitos");
		}
		
		teclado.close();

	}

}
