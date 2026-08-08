package problemas;

import java.util.*;

public class Problema1043 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		float valorA = teclado.nextFloat();
		float valorB = teclado.nextFloat();
		float valorC = teclado.nextFloat();
		
		float area = ((valorA + valorB) * valorC)/2;
		float perimetro = valorA + valorB + valorC;
		if (valorA + valorB > valorC && valorA+valorC > valorB && valorB + valorC > valorA)
		{
			System.out.printf("Perimetro = %.1f%n", perimetro);
		}
		else {
			System.out.printf("Area = %.1f%n",area);
		}
		
		teclado.close();		

	}

}
