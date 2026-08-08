//Para ler e escrever dados em Java, aqui na DIO padronizamos da seguinte forma:
// - new Scanner(Systen.in): para criar um leitor de entrada, com métodos uteis
//com prefixo "next";
// - System.out.println: imprime um texto de Saída (Output) e pulando uma linha;

import java.util.Scanner;

public class aprendendo_Logica {
    public static void main(String[] args) {
        Scanner leitorDeEntrada = new Scanner(System.in);
        float valorSalario = leitorDeEntrada.nextFloat();
        float valorBeneficios = leitorDeEntrada.nextFloat();

        float valorImposto = 0;

        if(valorSalario >= 0 && valorSalario <= 1100){
            //Atribui a aliquota de 5% mediante o salário
            valorImposto = 0.05f * valorSalario;        }
        else if(valorSalario > 1100 && valorSalario <= 2500){
            //Atribui a aliquota de 10% mediante o salário
            valorImposto = 0.10f * valorSalario;        }
        else{
            //Atribui a aliquota de 15% mediante o salário
            valorImposto = 0.15f * valorSalario;        }
//Calcula e imprime a Saída (com 2 casas decimais)
        float saida = valorSalario - valorImposto + valorBeneficios;
        System.out.println(String.format("%.2f", saida));

    }
}