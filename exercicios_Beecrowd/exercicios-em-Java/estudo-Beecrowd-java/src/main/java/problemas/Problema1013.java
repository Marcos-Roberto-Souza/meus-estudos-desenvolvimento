package problemas;

import java.util.*;

public class Problema1013 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int primeiroNumero = teclado.nextInt();
		int segundoNumero = teclado.nextInt();
		int terceiroNumero = teclado.nextInt();
		
		int maiorEntreAB = (primeiroNumero + segundoNumero + Math.abs(primeiroNumero-segundoNumero))/2;
		int maiorEntreABC = (maiorEntreAB + terceiroNumero + Math.abs(maiorEntreAB - terceiroNumero))/2;
		
		System.out.println(maiorEntreABC + " eh o maior");
		
		teclado.close();

	}

}
