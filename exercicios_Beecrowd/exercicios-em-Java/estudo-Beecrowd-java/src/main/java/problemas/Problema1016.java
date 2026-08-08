package problemas;

import java.util.*;

public class Problema1016 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int distancia = teclado.nextInt();
		
		int carroY = 2;
		
		int calculoMinutos = distancia * carroY;
		
		System.out.println(calculoMinutos+ " minutos");
		
		teclado.close();

	}

}
