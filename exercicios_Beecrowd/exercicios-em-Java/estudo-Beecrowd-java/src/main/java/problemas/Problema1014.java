package problemas;

import java.util.*;

public class Problema1014 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int distanciaPercorrida = teclado.nextInt();
		float combustivelGasto = teclado.nextFloat();
		
		double consumoAutomovel = distanciaPercorrida / combustivelGasto; 
		
		System.out.printf("%.3f km/l%n", consumoAutomovel);
		
		teclado.close();
		
	}

}
