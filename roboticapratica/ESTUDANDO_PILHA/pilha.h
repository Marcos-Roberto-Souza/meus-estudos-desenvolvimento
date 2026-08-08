typedef int TipoItem;
const int max_itens = 100;
class pilha{
    private:
    int tamanho;
    TipoItem* estrutura;

    public:
    pilha(); // construtora
    ~pilha();//destrutora
    bool estacheia();//verifica se a pilha esta cheia
    bool estavazia();//verifica se a pilha esta vazia
    void inserir(TipoItem item);//push inserir itens
    TipoItem remover();//Remover ou pop
    void imprimir();//print
    int qualtamanho();//Qual o tamnho lenght
    
};