package problemas;

import java.util.*;

public class Problema1036 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		double valorA = teclado.nextDouble();
		double valorB = teclado.nextDouble();
		double valorC = teclado.nextDouble();
		
		double delta = Math.pow(valorB,2) - (4*valorA*valorC);
		
		if (delta < 0 || valorA <= 0 || valorB <= 0 || valorC <=0){
			System.out.println("Impossivel calcular");
		}else {
			double R1 = (-valorB  + Math.sqrt(delta))/(2.0*valorA);
			double R2 = (-valorB  - Math.sqrt(delta))/(2.0*valorA);		
			System.out.printf("R1 = %.5f%n", R1);
			System.out.printf("R2 = %.5f%n", R2);
		}
		
		teclado.close();
		
	}

}
