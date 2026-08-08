// Pilha Dinâmica = Dynamic Stack

typedef int TipoItem;

struct No //Node
{
    TipoItem valor;
    No* proximo;
};

class pilhadinamica{
    private:
    No* NoTopo;

    public:
    pilhadinamica();//construtor
    ~pilhadinamica();//destrutor
    bool estavazio();//Is Empty
    bool estacheio();//tem item na memória
    void inserir(TipoItem item);//push
    TipoItem remover();//pop Remover
    void imprimir();
};