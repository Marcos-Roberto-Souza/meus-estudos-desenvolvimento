package problemas;

//Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.
//
//Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.
//
//Entrada
//Como entrada, na primeira linha vai haver a descrição “Dia”, seguido de um espaço e o dia do mês no qual o evento vai começar. Na linha seguinte, será informado o momento no qual o evento vai iniciar, no formato hh : mm : ss. Na terceira e quarta linha de entrada haverá outra informação no mesmo formato das duas primeiras linhas, indicando o término do evento.
//
//Saída
//Na saída, deve ser apresentada a duração do evento, no seguinte formato:
//
//W dia(s)
//X hora(s)
//Y minuto(s)
//Z segundo(s)
//
//Obs: Considere que o evento do caso de teste para o problema tem duração mínima de 1 minuto.

import java.util.*;

public class Problema1061 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
				
		int diaInicio = Integer.parseInt(teclado.nextLine().split(" ")[1]);
		
		String[] inicio = teclado.nextLine().split(" : ");
		
		int hInicio = Integer.parseInt(inicio[0]);
		int mInicio = Integer.parseInt(inicio[1]);
		int sInicio = Integer.parseInt(inicio[2]);
		
		int diaFim = Integer.parseInt(teclado.nextLine().split(" ")[1]);
		
		String[] fim = teclado.nextLine().split(" : ");
		
		int hFim = Integer.parseInt(fim[0]);
		int mFim = Integer.parseInt(fim[1]);
		int sFim = Integer.parseInt(fim[2]);
		
		int inicioTotal =
			    diaInicio * 24 * 3600 +
			    hInicio * 3600 +
			    mInicio * 60 +
			    sInicio;

			int fimTotal =
			    diaFim * 24 * 3600 +
			    hFim * 3600 +
			    mFim * 60 +
			    sFim;

			int diferenca = fimTotal - inicioTotal;

			int dia = diferenca / (24 * 3600);
			diferenca %= (24 * 3600);

			int hora = diferenca / 3600;
			diferenca %= 3600;

			int minuto = diferenca / 60;
			diferenca %= 60;

			int segundo = diferenca;
		
		System.out.println(dia + " dia(s)");
		System.out.println(hora + " hora(s)");
		System.out.println(minuto + " minuto(s)");
		System.out.println(segundo + " segundo(s)");
		
		teclado.close();

	}

}
