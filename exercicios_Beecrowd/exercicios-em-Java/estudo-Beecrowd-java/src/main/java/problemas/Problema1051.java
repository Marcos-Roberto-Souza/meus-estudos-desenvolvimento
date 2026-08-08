package problemas;

import java.util.*;

public class Problema1051 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		float impostoRenda = 0;
		
		float rendaSalarial = teclado.nextFloat();
		if (rendaSalarial > 0.0 && rendaSalarial <= 2000.00) 
		{
			System.out.println("Isento");
		}
		else if (rendaSalarial > 2000.00 && rendaSalarial <= 3000.00) 
		{
			impostoRenda = (float)((rendaSalarial - 2000.00)*0.08);
			System.out.printf("R$ %.2f%n", impostoRenda);		
		}	
		else if (rendaSalarial > 3000.00 && rendaSalarial <= 4500.00) 
		{
			impostoRenda = (float) (1000 * 0.08);
			impostoRenda += (float)((rendaSalarial-3000)* 0.18);
			System.out.printf("R$ %.2f%n", impostoRenda);

		}
		else if (rendaSalarial > 4500.00) 
		{
			impostoRenda = (float)(1000 * 0.08);
			impostoRenda += 1500*0.18;
			impostoRenda += (rendaSalarial-4500)* 0.28;
			System.out.printf("R$ %.2f%n", impostoRenda);

		}
		teclado.close();
				    
	}

}
