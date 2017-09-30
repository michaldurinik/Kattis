//https://open.kattis.com/problems/nastyhacks
#include <iostream>
using namespace std;

int main(){
    long long r, e, c;
    int lines;

    cin >> lines;
    while (cin >> r >> e >> c){
        if (r == (e - c)){
            cout << "does not matter" << endl;
        }
        else if (r > (e - c)){
            cout << "do not advertise" << endl;
        }
        else cout << "advertise" << endl;
    }
    return 0;
}

