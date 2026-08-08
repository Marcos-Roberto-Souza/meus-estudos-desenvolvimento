package problemas;

//Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, 
//da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, 
//através das três palavras fornecidas.
//
//Vertebrado >> ave      >> carnivoro >> aguia
//Vertebrado >> ave      >> onivoro   >> pomba
//Vertebrado >> mamifero >> onivoro   >> homem
//Vertebrado >> mamifero >>herbivoro  >> vaca
//
//Invertebrado >> inseto  >> hematofago  >> pulga
//Invertebrado >> inseto  >> herbivoro   >> lagarta
//Invertebrado >> anelideo >> hematofago >> sanguessuga
//Invertebrado >> anelideo >> onivoro    >> minhoca
//Entrada
//A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.
//
//Saída
//Imprima o nome do animal correspondente à entrada fornecida.

import java.util.*;

public class Problema1049 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner teclado = new Scanner(System.in);
		
		String primeiraPalavra = teclado.next();
		String segundaPalavra = teclado.next();
		String terceiraPalavra = teclado.next();
		
		if (primeiraPalavra.equals("vertebrado"))
		{			
			if (segundaPalavra.equals("ave")) 
			{				
				if (terceiraPalavra.equals("carnivoro")) 
				{
					System.out.println("aguia");
				}
				else 
				{
					System.out.println("pomba");
				}
			}
			else if (segundaPalavra.equals("mamifero")) 
			{
				if (terceiraPalavra.equals("onivoro")) 
				{
					System.out.println("homem");
				}
				else 
				{
					System.out.println("vaca");
				}
			}
		}
		else if (primeiraPalavra.equals("invertebrado"))
		{
			if (segundaPalavra.equals("inseto")) 
			{
				if (terceiraPalavra.equals("hematofago")) 
				{
					System.out.println("pulga");
				}
				else 
				{
					System.out.println("lagarta");
				}
			}
			else if(segundaPalavra.equals("anelideo"))
			{
				if (terceiraPalavra.equals("hematofago")) 
				{
					System.out.println("sanguessuga");
				}
				else
				{
					System.out.println("minhoca");
				}
			}
		}
		teclado.close();

	}

}
