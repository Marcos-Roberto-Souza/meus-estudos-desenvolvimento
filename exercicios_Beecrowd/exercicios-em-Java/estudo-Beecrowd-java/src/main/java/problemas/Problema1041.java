package problemas;

//Leia 2 valores com uma casa decimal (x e y), 
//que devem representar as coordenadas de um ponto em um plano. 
//A seguir, determine qual o quadrante ao qual pertence o ponto, 
//ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
//
//		|y
// 	Q2	|	Q1
//------|---------x
//	Q3 	|	Q4
//		|
//
//Se o ponto estiver na origem, escreva a mensagem “Origem”.
//
//Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.
//
//Entrada
//A entrada contem as coordenadas de um ponto.
//
//Saída
//A saída deve apresentar o quadrante em que o ponto se encontra.		
		
import java.util.*;

public class Problema1041 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		float primeiroPonto = teclado.nextFloat();
		float segundoPonto = teclado.nextFloat();
		
		if (primeiroPonto == 0.0 && segundoPonto == 0.0) 
		{
			System.out.println("Origem");
		}
		else if(primeiroPonto == 0.0) {
			System.out.println("Eixo Y");
		}
		else if(segundoPonto == 0.0) 
		{
			System.out.println("Eixo X");
		}
		else if(primeiroPonto > 0.0 && segundoPonto > 0.0) 
		{
			System.out.println("Q1");
		}
		else if(primeiroPonto < 0.0 && segundoPonto > 0.0) 
		{
			System.out.println("Q2");
		}
		else if(primeiroPonto < 0.0 && segundoPonto < 0.0) 
		{
			System.out.println("Q3");
		}
		else if(primeiroPonto > 0.0 && segundoPonto < 0.0) 
		{
			System.out.println("Q4");
		}
		teclado.close();
		
		

	}

}
