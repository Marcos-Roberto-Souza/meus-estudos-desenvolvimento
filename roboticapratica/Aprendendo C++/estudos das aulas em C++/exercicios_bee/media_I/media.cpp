#include <iomanip>
#include <iostream>

using namespace std;

int main(){
    double a,b,med;

    cin >> a;
    cin >> b;

    med = ((a*3.5) + (b*7.5))/11;

    cout << fixed << setprecision(5);
    
    cout << "MEDIA = " << med << endl;

    return 0 ;

}