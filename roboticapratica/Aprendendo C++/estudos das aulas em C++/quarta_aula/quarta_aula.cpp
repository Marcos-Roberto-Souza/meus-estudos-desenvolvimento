#include <iostream>

using namespace std;

int main(){
    int num1;
    int count = 0;
    int amount = 0;

    while(count < 10){

        cout << "Digite um Numero (" << count <<")" << endl;
        cin >> num1;

        if(num1 < 5){
            amount++;
        }
        count++;
    }

    cout << "Quantidade de Numeros Menores que 5: [" << amount << "]" << endl;

    return 0;
}