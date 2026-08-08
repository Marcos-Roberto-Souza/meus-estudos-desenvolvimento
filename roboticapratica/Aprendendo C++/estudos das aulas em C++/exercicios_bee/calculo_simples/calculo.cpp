#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int a,b,c,d;
    double va,vb,vp;

    cin >> a >> b >> va;
    cin >> c >> d >> vb;

    vp = (b*va)+(d*vb);

    cout << fixed << setprecision(2);
    cout << "VALOR A PAGAR: R$ " << vp << endl;

    return 0;
}