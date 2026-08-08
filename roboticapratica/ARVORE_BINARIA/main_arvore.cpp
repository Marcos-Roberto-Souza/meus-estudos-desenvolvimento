#include <iostream>
#include "arvorebinaria.h"

using namespace std;

int main(){
    ArvoreBinariadeBusca Arvorealunos;
    int opcao, ra, imp;
    string nome;
    bool busca = false;

    do{
        cout << "Digite 0 para PARAR o algoritmo!\n";
        cout << "Digite 1 para INSERIR um elemento!\n";
        cout << "Digite 2 para REMOVER um elemento!\n";
        cout << "Digite 3 para BUSCAR um elemento!\n";
        cout << "Digite 4 para IMPRIMIR a arvore!\n";
        cin >> opcao;
        
        if(opcao == 1){
            cout << "Digite o nome do aluno:\n";
            cin >> nome;
            cout << "Digite o RA do aluno:\n";
            cin >> ra;
            Aluno aluno(ra,nome);
        
        if(Arvorealunos.estacheio()){
            cout << "A Árvore esta cheia!**\n";
            cout << "Não foi possivel inserir o elemento!\n";
        } else{
            Arvorealunos.inserir(aluno);
        }
        }else if(opcao == 2){
            cout << "Digite o RA do aluno a ser REMOVIDO!\n";
            cin >> ra;
            Aluno aluno(ra," ");
            Arvorealunos.remover(aluno);

        }else if(opcao == 3){
            cout << "Digite o RA do aluno a ser buscado!\n";
            cin >> ra;
            Aluno aluno(ra," ");
            Arvorealunos.buscar(aluno, busca);
            if(busca){
                cout << "Elemento encontrado!\n";
                cout << "Nome: " << aluno.obterNome() << endl;
                cout << "RA " << aluno.obterRa() << endl;
            } else{
                cout << "Elemento nao encontrado!\n";
            }
        }else if(opcao == 4){
            cout << "Digite 1 para fazer a impressão em Pré Ordem!\n";
            cout << "Digite 2 para fazer a impressão em Ordem!\n";
            cout << "Digite 3 para fazer a impressão em Pós Ordem!\n";
            cin >> imp;
            if(imp == 1){                
                Arvorealunos.imprimirpreordem(Arvorealunos.obterRaiz());
            }else if (imp == 2){                
                Arvorealunos.imprimiremordem(Arvorealunos.obterRaiz());
            } else{
                Arvorealunos.imprimirposordem(Arvorealunos.obterRaiz());
            }
        }
    } while (opcao != 0);

    return 0;
}