#include <iostream>
#include <iomanip>

using namespace std;

int main() {
    double a,b,c,med;

    cin >> a ;
    cin >> b;
    cin >> c;

    med = ((a*2)+(b*3)+(c*5))/10;

    cout << fixed << setprecision(1);
    cout << "MEDIA = " << med << endl;

    return 0;
}