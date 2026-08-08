package problemas;
import java.util.Scanner;

public class Problema1005 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		double nota1 = entrada.nextDouble();
		double nota2 = entrada.nextDouble();
		
		double media = ((nota1*3.5) + (nota2*7.5))/11;
		System.out.printf("MEDIA = %.5f%n", media);
		
		entrada.close();
	}

}
