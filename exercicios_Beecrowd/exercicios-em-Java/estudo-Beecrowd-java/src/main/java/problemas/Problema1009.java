package problemas;
import java.util.*;

public class Problema1009 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		var nome = teclado.next();
		double salarioFixo = teclado.nextDouble();
		double montanteTotal = teclado.nextDouble();
		
		double totalBonus = (montanteTotal*0.15) + salarioFixo;
		
		System.out.printf("TOTAL = R$ %.2f%n", totalBonus);
		
		teclado.close();		

	}

}
