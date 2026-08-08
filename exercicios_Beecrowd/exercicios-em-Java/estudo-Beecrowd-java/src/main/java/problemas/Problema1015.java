package problemas;

import java.util.*;

public class Problema1015 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		float pontoX1 = teclado.nextFloat();
		float pontoY1 = teclado.nextFloat();
		float pontoX2 = teclado.nextFloat();
		float pontoY2 = teclado.nextFloat();
		
		double distancia = Math.sqrt(Math.pow(pontoX2 - pontoX1,2) + Math.pow(pontoY2 - pontoY1,2));
		
		System.out.printf("%.4f%n",distancia);
		
		teclado.close();

	}

}
