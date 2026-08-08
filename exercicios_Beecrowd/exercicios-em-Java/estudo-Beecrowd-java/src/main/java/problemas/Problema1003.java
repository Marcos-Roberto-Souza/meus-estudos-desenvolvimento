package problemas;

import java.util.Scanner;

public class Problema1003 {
	public static void main(String[] args) {
		//TODO auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		int primeiroValor = entrada.nextInt();
		int segundoValor = entrada.nextInt();
		
		int soma = primeiroValor + segundoValor;
		
		System.out.println("SOMA = "+ soma);
		
		entrada.close();
	}

}
