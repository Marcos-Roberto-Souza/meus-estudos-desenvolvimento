package problemas;

import java.util.*;

public class Problema1045 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		Double[] lados =  Arrays.stream(teclado.nextLine().split(" "))
				.map(Double::parseDouble)
				.sorted(Collections.reverseOrder())
				.toArray(Double[]::new);
		
		double A = lados[0];
		double B = lados[1];
		double C = lados[2];
		
		double a2 = A*A;
		double b2 = B*B;
		double c2 = C*C;
		
		
		if (A >= B+C)
		{
			System.out.println("NAO FORMA TRIANGULO");
		}
		else {
			if (a2 == b2+ c2)
			{
				System.out.println("TRIANGULO RETANGULO");
			}
			if (a2 > b2 + c2)
			{
				System.out.println("TRIANGULO OBTUSANGULO");
			}
			if (a2 < b2 + c2)
			{
				System.out.println("TRIANGULO ACUTANGULO");
			}
			if (A == B && B==C)
			{
				System.out.println("TRIANGULO EQUILATERO");
			}
			else if (A==B || A==C || B == C)
			{
				System.out.println("TRIANGULO ISOSCELES");
			}
		}
		teclado.close();		 
		
	}

}
