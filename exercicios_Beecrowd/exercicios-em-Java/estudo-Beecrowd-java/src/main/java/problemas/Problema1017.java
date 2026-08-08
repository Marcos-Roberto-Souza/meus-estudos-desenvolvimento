package problemas;

import java.util.*;

public class Problema1017 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int tempoGastoViagem = teclado.nextInt();
		int velociadaMedia = teclado.nextInt();
		
		double quantidadeLitros = (tempoGastoViagem * velociadaMedia) / 12.0;
		
		System.out.printf("%.3f%n", quantidadeLitros);
		
		teclado.close();

	}

}
