#include <iostream>
#include "pilhadinamica.h"
#include <cstddef> //null

using namespace std;


    pilhadinamica::pilhadinamica()//construtor
    {
        NoTopo = NULL;
    }
    pilhadinamica::~pilhadinamica()//destrutor
    {
        No* NoTemp;
        while(NoTopo != NULL){
            NoTemp = NoTopo;
            NoTopo = NoTopo->proximo;
            delete NoTemp;
        }
    }
    bool pilhadinamica::estavazio()//Is Empty
    {
        return(NoTopo == NULL);
    }
    bool pilhadinamica::estacheio()//tem item na memória
    {
        No* NoNovo;
        try{
            NoNovo = new No;
            delete NoNovo;
            return false;

        } catch(bad_alloc exception){
            return true;

        }
    }
    void pilhadinamica::inserir(TipoItem item)//push
    {
        if (estacheio()){
            cout << "A Pilha esta cheia!\n";
            cout << "Nao foi possivel inserir este elemento!\n";
        }else {
            No* NoNovo = new No;
            NoNovo->valor = item;
            NoNovo->proximo = NoTopo;
            NoTopo = NoNovo;
        }
    }
    TipoItem pilhadinamica::remover()//pop Remover
    {
        if(estavazio()){
            cout << "A Pilha esta vazia!\n";
            cout << "Nao foi possivel Remover nenhum elemento";
            return 0;
        }else{
            No* NoTemp;
            NoTemp = NoTopo;
            TipoItem item = NoTopo->valor;
            NoTopo = NoTopo->proximo;
            delete NoTemp;
            return item;
        }
    }
    void pilhadinamica::imprimir()// print
    {
        No* NoTemp = NoTopo;
        cout << "Pilha: [";
        while(NoTemp != NULL){
            cout << NoTemp->valor << " ";
            NoTemp = NoTemp->proximo;

        }
        cout << "]\n";
    }