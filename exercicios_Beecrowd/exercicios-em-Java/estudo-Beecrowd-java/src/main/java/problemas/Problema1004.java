package problemas;
import java.util.Scanner;

public class Problema1004 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner entrada = new Scanner(System.in);
		
		int primeiroNumero = entrada.nextInt();
		int segundoNumero = entrada.nextInt();
		
		int produto = primeiroNumero * segundoNumero;
		
		System.out.println("PROD = "+ produto);
		
		entrada.close();

	}

}
