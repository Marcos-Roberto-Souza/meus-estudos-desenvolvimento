#include <iostream>
#include "pilhadinamica.h"

using namespace std;

int main(){
    pilhadinamica pilha1;
    TipoItem item;
    int opcao;
    cout << "Programa gerador de pilha:\n";

    do{
        cout << "Digite 0 para PARAR o programa!\n";
        cout << "Digite 1 para INSERIR  Elemento!\n";
        cout << "Digite 2 para REMOVER Elemento!\n";
        cout << "Digite 3 para IMPRIMIR os Elementos da Pilha!\n";
        cin >> opcao;
        if(opcao == 1){
            cout<< "Digite o Elemento a Ser Inserido:\n";
            cin >> item;
            pilha1.inserir(item);
        }else if(opcao == 2){
            item = pilha1.remover();
            cout << "Elemento REMOVIDO: " << item << endl;
        }else if(opcao == 3){
            pilha1.imprimir();
        }

    }while (opcao != 0);
    
    return 0;

};