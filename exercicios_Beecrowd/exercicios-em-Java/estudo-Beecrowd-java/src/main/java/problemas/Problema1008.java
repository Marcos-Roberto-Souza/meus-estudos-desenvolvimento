package problemas;
import java.util.*;

public class Problema1008 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner digite = new Scanner(System.in);
		
		int numeroFuncionario = digite.nextInt();
		int quantidadeHorasTrabalhada = digite.nextInt();
		double valorDaHoraTrabalhada = digite.nextDouble();
		
		double calculoSalario = quantidadeHorasTrabalhada * valorDaHoraTrabalhada;
		
		System.out.printf("NUMBER = %d%n", numeroFuncionario);
		System.out.printf("SALARY = U$ %.2f%n", calculoSalario);
		
		digite.close();		

	}

}
