// Dynamic Queue

typedef int TipoItem;

struct No
{
    public:
    TipoItem valor;
    No* proximo;

};
class filadinamica{
    private:
    No* primeiro;//front
    No* ultimo; // rear

    public:
    filadinamica();//construtor
    ~filadinamica();//Destrutor
    bool estavazio();//isEmpty
    bool estacheio();//isFull
    void inserir(TipoItem item);//EnQueue push
    TipoItem remover();// dequeue Pop
    void imprimir();//print

};