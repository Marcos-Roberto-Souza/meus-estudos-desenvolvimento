#include <iostream>
#include "fila.h"

using namespace std;   
    
    fila::fila()//construtor
    {
        primeiro = 0;
        ultimo = 0;
        estrutura = new TipoItem2[max_itens];
    }
    fila::~fila()//destrutor
    {
        delete [] estrutura;
    }
    bool fila::estavazio()//isEmpty
    {
        return (primeiro == ultimo);
    }
    bool fila::estacheio()//isFull
    {
        return (ultimo-primeiro == max_itens);
    }
    void fila::inserir(TipoItem2 item)//push enqueue
    {
        if(estacheio()){
            cout << "A fila esta cheia\n";
            cout << "Esse elemento nao pode ser inserido\n";
        }
        else{
            estrutura[ultimo % max_itens] = item;
            ultimo++;
        }
    }
    TipoItem2 fila::remover()
    {
        if(estavazio()){
            cout << "A fila esta vazia!\n";
            cout << "Nenhum elemento foi Removido!\n";
            return 0;
        }else{
            primeiro++;
            return estrutura[(primeiro-1) % max_itens];            
        }
    }
    void fila::imprimir()//print
    {
        cout << "Fila:[";
        for (int i = primeiro; i < ultimo; i++){
            cout << estrutura[i % max_itens] << " ";
            cout << "]\n";
        }
    }