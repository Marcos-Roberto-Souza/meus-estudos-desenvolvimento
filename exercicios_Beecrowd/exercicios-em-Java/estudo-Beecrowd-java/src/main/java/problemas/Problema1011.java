package problemas;

import java.util.*;

public class Problema1011 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		double valorRaio = teclado.nextDouble();
		
		double PI = 3.14159; 
		
		double volume = 4/3.0*PI*Math.pow(valorRaio,3);
		
		System.out.printf("VOLUME = %.3f%n", volume);
		
		teclado.close();

	}

}
