package problemas;

import java.util.*;

public class Problema1010 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int codigoPeca1 = teclado.nextInt();
		int quantdidadePeca1 = teclado.nextInt(); 
		double valorPeca1 = teclado.nextDouble();
		
		int codigoPeca2 = teclado.nextInt(); 
		int quantdidadePeca2 = teclado.nextInt(); 
		double valorPeca2 = teclado.nextDouble();
		
		double fechandoCompra = quantdidadePeca1 * valorPeca1 + quantdidadePeca2 * valorPeca2;
		
		System.out.printf("VALOR A PAGAR: R$ %.2f%n", fechandoCompra);
		
		teclado.close();

	}

}
