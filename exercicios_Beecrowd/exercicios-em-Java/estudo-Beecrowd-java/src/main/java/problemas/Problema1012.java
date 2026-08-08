package problemas;

import java.util.*;

public class Problema1012 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		float ladoA = teclado.nextFloat();
		float ladoB = teclado.nextFloat();
		float ladoC = teclado.nextFloat();
		
		double PI = 3.14159;
		
		double triangulo = ladoA * ladoC / 2;
		double circulo = Math.pow(ladoC,2) * PI;
		double trapezio = (ladoA + ladoB) * ladoC /2;
		double quadrado = Math.pow(ladoB,2);
		double retangulo = ladoA * ladoB;
				
		System.out.printf("TRIANGULO: %.3f%n", triangulo);
		System.out.printf("CIRCULO: %.3f%n", circulo);
		System.out.printf("TRAPEZIO: %.3f%n", trapezio);
		System.out.printf("QUADRADO: %.3f%n", quadrado);
		System.out.printf("RETANGULO: %.3f%n", retangulo);
		
		teclado.close();		

	}

}
