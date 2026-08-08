package problemas;

//Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. 
//A seguir calcule a duração do jogo.
//
//Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
//
//Entrada
//Quatro números inteiros representando a hora de início e fim do jogo.
//
//Saída
//Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
//
//Exemplo de Entrada	
//7 8 9 10
//
//Exemplo de Saída
//
//O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)

import java.util.*;

public class Problema1047 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int horaInicial = teclado.nextInt();
		int minutoInicial = teclado.nextInt();
		int horaFinal = teclado.nextInt();
		int minutoFinal = teclado.nextInt();
		
		int inicio = horaInicial*60+minutoInicial;
		int fim = horaFinal*60 + minutoFinal;
		
		if (fim <= inicio)
		{
			fim+=24*60;
		}			
		
		int duracao = fim-inicio;
		
		int hora = duracao/60;
		int minuto = duracao%60;
		
				
		System.out.printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)%n", hora, minuto);
		
		teclado.close();

	}

}
