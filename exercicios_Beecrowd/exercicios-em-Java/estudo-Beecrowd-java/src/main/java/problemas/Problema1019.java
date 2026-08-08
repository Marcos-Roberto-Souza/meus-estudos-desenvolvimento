package problemas;

import java.util.*;

public class Problema1019 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int tempo = teclado.nextInt();
		int horas = tempo / 3600;
		tempo = tempo%3600;
		
		int minutos = tempo/60;
		int segundos = tempo%60;
				
		
		System.out.println(horas + ":" + minutos + ":" + segundos);
		
		teclado.close();

	}

}
