//https://open.kattis.com/problems/herman
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    double radius;
    cin >> radius;
    cout.precision(17);
    cout << radius * radius * M_PI << endl;
    cout << radius * radius * 2 << endl;

    return 0;
}
