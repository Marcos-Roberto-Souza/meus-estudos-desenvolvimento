package problemas;

import java.util.*;

public class Problema1020 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		int idadeDias = teclado.nextInt();
		
		int ano = idadeDias/365;
		
		idadeDias = idadeDias%365;
		
		int mes = idadeDias/30;
		
		int dia = idadeDias%30;
		
		System.out.println(ano+" ano(s)");
		System.out.println(mes + " mes(es)");
		System.out.println(dia + " dia(s)");
		
		teclado.close();

	}

}
