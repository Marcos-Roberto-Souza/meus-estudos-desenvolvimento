package problemas;

import java.util.*;

public class Problema1018 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int deposito = teclado.nextInt();
		
		System.out.println(deposito);
		
		int[] cedulas = {100, 50, 20, 10, 5, 2, 1};
		
		for (int cedula : cedulas) {
			int quantidade = deposito / cedula;
			System.out.println(quantidade + " nota(s) de R$ " + cedula +  ",00");
			deposito %= cedula;
		 }
		 
		 teclado.close();		 

	}

}
