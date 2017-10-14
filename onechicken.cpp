//https://open.kattis.com/problems/onechicken
#include<iostream>
#include<cmath>
using namespace std;

int main(){
    int people, chickens, difference;
    string pieces = " pieces ";

    cin >> people >> chickens;
    difference = people - chickens;

    if(abs(difference) == 1)
        pieces = " piece ";

    if(difference < 0)
        cout << "Dr. Chaz will have " << abs(difference) << pieces << "of chicken left over!" << endl;
    else cout << "Dr. Chaz needs " << difference << " more" << pieces  << "of chicken!" << endl;

    return 0;
}

