package problemas;

import java.util.*;

public class Problema1007 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner digite = new Scanner(System.in);
		
		int valor1 = digite.nextInt();
		int valor2 = digite.nextInt();
		int valor3 = digite.nextInt();
		int valor4 = digite.nextInt();
		
		int diferenca = valor1*valor2 - valor3*valor4;
		
		System.out.printf("DIFERENCA = %d%n", diferenca);
		
		digite.close();
		
		

	}

}
