#include <iostream>
using namespace std;

int main() {
    int num1;
    int num2;

    cout << "Digite o Primeiro Numero: ";
    cin >> num1;
    cout << "Digite o Segundo Numero: ";
    cin >> num2;

    if (num1 == num2)
    cout << num1 << "==" << num2 << endl;

    if (num1 != num2)
    cout << num1 << "!= " << num2 << endl;

    if (num1 < num2)
    cout << num1 << " < " << num2 << endl;

    if (num1 > num2)
    cout << num1 << " > " << num2 << endl;

    if (num1 <= num2)
    cout << num1 << " <= " << num2 << endl;

    if (num1 >= num2)
    cout << num1 << " >= " << num2 << endl;

    return 0;
}
