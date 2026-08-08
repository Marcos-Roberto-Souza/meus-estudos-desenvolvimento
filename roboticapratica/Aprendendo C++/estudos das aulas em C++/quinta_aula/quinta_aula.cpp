#include <iostream>

using namespace std;

int main(){
    int total;
    int number = 2;

    for (number; number <= 20; number +=2)
    total += number; 

    cout << "A soma da Serie e: " << total << endl;

    return 0;
}