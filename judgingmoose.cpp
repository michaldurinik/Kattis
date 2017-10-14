//https://open.kattis.com/problems/judgingmoose
#include <iostream>
using namespace std;

int main(){
    int x, y, bigger;
    cin >> x; 
    cin >> y;

    if(x == y){
        if(x == 0){
        
            cout << "Not a moose" << endl;
        }
        else{
            cout << "Even " << (2 * x) << endl;
        }
    }
    else{
        if(x > y){
            bigger = x;
        }
        else{
            bigger = y;
        }

    cout << "Odd " << (bigger * 2) << endl;
    }
    return 0;
}
