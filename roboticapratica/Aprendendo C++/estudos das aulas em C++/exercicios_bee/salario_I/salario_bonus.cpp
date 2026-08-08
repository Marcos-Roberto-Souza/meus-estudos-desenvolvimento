#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    string a;
    double sal,vend, calcula;

    cin >> a;
    cin >> sal;
    cin >> vend;

    calcula = ((vend*15)/100)+sal;

    cout << fixed << setprecision(2);
    cout << "TOTAL = R$ " << calcula << endl;

    return 0;
}