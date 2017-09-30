//https://open.kattis.com/problems/deathknight
#include <iostream>
#include <string>
using namespace std;

int main(){
    int total = 0;
    int cases;
    string abilities;

    cin >> cases;
    while (cin >> abilities){
        if (abilities.find("CD") == string::npos)
            total++;
    }
    cout << total << endl;
    return 0;    
}
