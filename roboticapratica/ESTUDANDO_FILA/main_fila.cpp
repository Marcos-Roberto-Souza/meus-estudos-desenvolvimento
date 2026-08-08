#include <iostream>
#include "fila.h"

using namespace std;

int main(){
    fila fila1;
    int opcao;
    TipoItem2 item;
    cout << "Programa Gerador De Filas:\n";
    do{
        cout << "Digite 0 para parar o Programa!\n";
        cout << "Digite 1 para Inserir o Elemento!\n";
        cout << "Digite 2 para Remover um Elemento!\n";
        cout << "Digite 3 para Imprimir a Fila\n!";
        cin >> opcao;
        if(opcao == 1){
            cout << "Digite o elemento a ser inserido na Fila";
            cin >> item;
            fila1.inserir(item);
        }else if(opcao == 2){
            item = fila1.remover();
            cout << "O Elemento removido e:" << item << endl;
        }else if(opcao == 3){
            fila1.imprimir();
        }


    }while(opcao !=0);

    return 0;
}