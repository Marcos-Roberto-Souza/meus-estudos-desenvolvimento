package problemas;

import java.util.*;

public class Problema1006 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner entrada = new Scanner(System.in);
		
		double valorA = entrada.nextDouble();
		double valorB = entrada.nextDouble();
		double valorC = entrada.nextDouble();
		
		double media = ((valorA*2)+ (valorB*3)+(valorC*5))/10;
		
		System.out.printf("MEDIA = %.1f%n", media);
		
		entrada.close();
		
		

	}

}
