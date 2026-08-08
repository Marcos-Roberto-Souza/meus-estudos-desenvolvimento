#include "aluno.h"

class Hash{
    private:
    int FuncaoHash(Aluno aluno);
    int max_itens; //maximo de itens no vetor
    int max_posicoes; //maxima posicao no vetor
    int quant_itens; //quantidade de itens no vetor
    Aluno* estrutura; // vetor que chama a estrutura aluno para adicionar itens no vetor

    public:
    Hash(int tam_vetor, int max);// construtor
    ~Hash(); // destrutor
    bool estacheio(); // verificar se estar cheio
    int obterTamanhoAtual(); //obter o tamanho do vertor atual
    void inserir(Aluno aluno); //inserir alunos
    void deletar(Aluno aluno); // remover alunos
    void buscar(Aluno& aluno,bool& busca); // busca por referencia
    void imprimir(); // imprimir 
};