#include <iostream>
#include "hash.h"

using namespace std;

int main(){
    cout << "PROGRAMA GERADOR DE HASH!\n";
    int tam_vetor, max;
    cout << "Digite o tamanho da Hash!\n";
    cin >> tam_vetor;
    cout << "Digite o numero maximo de elementos!\n";
    cin >> max;
    cout << "O fator de carga e: " << (float)max / (float)tam_vetor << endl;
    Hash alunohash(tam_vetor, max);
    int opcao;
    int ra;
    string nome;
    bool busca;

    do{
        cout << "Digite 0 para PARAR o algoritmo!\n";
        cout << "Digite 1 para INSERIR um elemento!\n";
        cout << "Digite 2 para REMOVER um elemento!\n";
        cout << "Digite 3 para BUSCAR um elemento!\n";
        cout << "Digite 4 para IMPRIMIR a Hash!\n";
        cin >> opcao;
        if(opcao == 1 ){
            cout << "Qual e o RA DO ALUNO?\n";
            cin >> ra;
            cout << "Qual e o NOME do ALUNO?\n";
            cin >> nome;
            Aluno aluno(ra,nome);
            alunohash.inserir(aluno);
        } else if(opcao == 2){
            cout << "Qual e o RA do Aluno a ser Removido?\n";
            cin >> ra;
            Aluno aluno(ra, " ");
            alunohash.deletar(aluno);

        }else if(opcao == 3){
            cout << "Qual e o RA do aluno a ser Buscado?\n";
            cin >> ra;
            Aluno aluno(ra, " ");
            alunohash.buscar(aluno,busca);
            if(busca){
                cout << "Aluno Encontrado:\n";
                cout << "RA: " << aluno.obterRa() << endl;
                cout << "NOME: " << aluno.obterNome() << endl;
            }else{
                cout << "Aluno nao encontrado!\n";
            }

        }else if(opcao == 4){
            alunohash.imprimir();

        }

    }while(opcao != 0);

    return 0;

}