package problemas;

import java.util.*;

public class Problema1044 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int valorA = teclado.nextInt();
		int valorB = teclado.nextInt();
		
		if (valorA%valorB==0 || valorB%valorA==0)
		{
			System.out.println("Sao Multiplos");
		}
		else if (valorA == valorB || valorA%valorB!=0)
		{
			System.out.println("Nao sao Multiplos");
		}
		
		teclado.close();

	}

}
