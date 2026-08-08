//fila estudos
typedef int TipoItem2;
const int max_itens = 100;

class fila{
    private:
    int primeiro,ultimo;
    TipoItem2* estrutura;

    public:
    fila();//construtor
    ~fila();//destrutor
    bool estavazio();//isEmpty
    bool estacheio();//isFull
    void inserir(TipoItem2 item);//push enqueue
    TipoItem2 remover();
    void imprimir();//print
};