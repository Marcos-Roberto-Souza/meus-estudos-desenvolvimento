#include <iostream>

using namespace std;
int main() {
    int number1;
    int number2;
    cout << "Enter two numbers: ";
    cin >> number1 >> number2;

    int sum = number1 + number2;
    int sub = number1 - number2;
    int mult = number1 * number2;
    int div = number1 / number2;
    float fdiv = (float)number1 / (float)number2;
    int res = number1 % number2;
    
    cout << "Sum: " << sum << endl;
    cout << "subtração: " << sub << endl;
    cout << "Multiplicação: " << mult << endl;
    cout << "Divisão Inteira: " << div << endl;
    cout << "Divisão Real: " << fdiv << endl;
    cout << "Resto: " << res << endl;

    return 0;
}