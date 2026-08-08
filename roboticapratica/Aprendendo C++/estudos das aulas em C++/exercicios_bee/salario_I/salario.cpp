#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int nf,nht;
    double sal,calcula;

    cin >> nf;
    cin >> nht;
    cin >> sal;

    calcula = nht * sal;

    cout << fixed << setprecision(2);
    cout << "NUMBER = " << nf << endl;
    cout << "SALARY = U$ " << calcula << endl;

    return 0;
}