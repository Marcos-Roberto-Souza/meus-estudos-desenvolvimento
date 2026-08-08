package problemas;

//Leia um número inteiro que representa um código de DDD para discagem interurbana. 
//Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:
//
//DDD		|		Destination
//----------------------------------			
//	61		>>	 Brasilia
//	71		>>	 Salvador
//	11		>>	 Sao Paulo
//	21		>>	 Rio de Janeiro
//	32		>> 	Juiz de Fora
//	19		>> 	Campinas
//	27		>> 	Vitoria
//	31		>> 	Belo Horizonte
//	
//	
//Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
//DDD nao cadastrado
//
//Entrada
//A entrada consiste de um único valor inteiro.
//
//Saída
//Imprima o nome da cidade correspondente ao DDD existente na entrada. 
//Imprima DDD nao cadastrado caso não existir DDD correspondente ao número digitado.
//
//Exemplo de Entrada	
//	11
//
//Exemplo de Saída
//	Sao Paulo

import java.util.*;

public class Problema1050 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int digiteDDD = teclado.nextInt();
		
		if (digiteDDD == 11) 
		{
			System.out.println("Sao Paulo");
		}
		else if (digiteDDD == 19) 
		{
			System.out.println("Campinas");
		}
		else if (digiteDDD == 21) 
		{
			System.out.println("Rio de Janeiro");
		}
		else if (digiteDDD == 27) 
		{
			System.out.println("Vitoria");
		}
		else if (digiteDDD == 31) 
		{
			System.out.println("Belo Horizonte");
		}
		else if (digiteDDD == 32) 
		{
			System.out.println("Juiz de Fora");
		}
		else if (digiteDDD == 71) 
		{
			System.out.println("Salvador");
		}
		else if (digiteDDD == 61) 
		{
			System.out.println("Brasilia");
		}
		else 
		{
			System.out.println("DDD nao cadastrado");
		}
		
		teclado.close();

	}

}
