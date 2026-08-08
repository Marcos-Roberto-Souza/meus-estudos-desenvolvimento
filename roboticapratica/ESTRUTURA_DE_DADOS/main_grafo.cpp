#include <iostream>
#include "grafo.h"

using namespace std;

int main(){
    int max, valorarestanula;
    cout << "Digite a Quantidade Maxima de Vertices: \n";
    cin >> max;
    cout << "Digite o Valor para representar a ausencia de aresta: \n";
    cin >> valorarestanula;
    Grafo grafo1(max, valorarestanula);
    TipoItem item1, item2;
    int opcao, valor, peso;

    do{
        cout << "Digite 0 para PARAR o algoritmo!\n";
        cout << "Digite 1 para INSERIR VERTICES!\n";
        cout << "Digite 2 para INSERIR ARESTA!\n";
        cout << "Digite 3 para IMPRIMIR GRAU VERTICE!\n";
        cout << "Digite 4 para IMPRIMIR PESO DA ARESTA\n";
        cout << "Digite 5 para IMPRIMIR MATRIZ ADJACENCIAS!\n";
        cout << "Digite 6 para IMPRIMIR LISTA DE VERTICES!\n";
        cin >> opcao;

        if(opcao == 1){
            cout << "Digite o elemento do vertice para ser INSERIDO:\n";
            cin >> item1;
            grafo1.inserevertice(item1);
        } else if (opcao == 2){
            cout << "Digite o vertice de SAIDA:\n";
            cin >> item1;
            cout << "Digite o vertice de ENTRADA:\n";
            cin >> item2;
            cout << "Digite o peso desta aresta:\n";
            cin >> peso;
            grafo1.inserearesta(item1, item2, peso);
        }else if (opcao == 3){
            cout << "Digite o Vertice que sera Calculado o Grau:\n";
            cin >> item1;
            valor = grafo1.obtergrau(item1);
            cout << "O Grau desse vertice e: " << valor << endl;
        }else if (opcao == 4){
            cout << "Digite o Vertice de SAIDA:\n";
            cin >> item1;
            cout << "Digite o vertice de ENTRADA:\n";
            cin >> item2;
            valor = grafo1.obterpeso(item1,item2);
            cout << "O peso dessa aresta e: " << valor << endl;
        } else if (opcao == 5){
            grafo1.imprimirmatriz();
        }else if (opcao == 6){
            grafo1.imprimirvertices();
        }
    }while (opcao != 0);

    return 0;
}
