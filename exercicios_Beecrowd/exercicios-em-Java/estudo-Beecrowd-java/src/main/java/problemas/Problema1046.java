package problemas;

//Leia a hora inicial e a hora final de um jogo. 
//A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, 
//tendo uma duração mínima de 1 hora e máxima de 24 horas.
//
//Entrada
//A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo.
//
//Saída
//Apresente a duração do jogo conforme exemplo abaixo.
//
//Exemplo de Entrada	
//	16  2
//
//Exemplo de Saída
//O JOGO DUROU 10 HORA(S)

import java.util.*;

public class Problema1046 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int horaInicial = teclado.nextInt();
		int horaFinal = teclado.nextInt();
		
		int termino = 0;
		
		
		
		if (horaInicial == horaFinal) 
		{
			termino = 24;
		}
		else if(horaInicial > horaFinal)
		{
			termino = (24 - horaInicial) + horaFinal;		
		}
		else 
		{
			termino = (horaFinal - horaInicial);
		}
		
		System.out.printf("O JOGO DUROU %d HORA(S)%n", termino);
		
		teclado.close();		

	}

}
