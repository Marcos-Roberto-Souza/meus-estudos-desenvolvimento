#include <iostream>
#include <iomanip>
#include <math.h>

using namespace std;

int main (){
    double r,ra;

    cin >> r;

    ra = ((4.0/3)*(3.14159*(pow(r,3))));

    cout << fixed << setprecision(3);
    cout << "VOLUME = " << ra << endl;

    return 0;

}