#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    int n;
    cin >> str >> n;
    if ((1<=str.length()<=10)&&(1<=n<=5))
        for (int i=0; i<n;i++)
            cout << str;   
    return 0;
}