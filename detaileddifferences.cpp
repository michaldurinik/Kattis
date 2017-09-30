//https://open.kattis.com/problems/detaileddifferences
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int cases;
    string s1;
    string s2;

    cin >> cases;
    while (cin >> s1 >> s2){
        cout << s1 << endl;
        cout << s2 << endl;
        for (int i = 0; i < s1.length(); i++){
            if (s1[i] != s2[i])
                cout << "*";
            else cout << ".";
            }
        cout << endl << endl;
        }
}
