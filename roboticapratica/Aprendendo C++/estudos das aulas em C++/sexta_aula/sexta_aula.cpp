#include <iostream>

using namespace std;

int main(){
    int cont;
    int num;
    int soma;
    do{
        cout << "Insira um novo Numero: "<< endl;
        cin >> num;

        soma += num;
        cont++;
        
    }   while(num != 0);

    float average = (float)soma/(float)(cont-1);
    cout << "A Media da Serie e: " << average << endl;

    return 0;
}