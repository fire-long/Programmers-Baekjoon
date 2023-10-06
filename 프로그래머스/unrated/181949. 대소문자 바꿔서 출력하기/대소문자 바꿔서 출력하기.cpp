#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    if (1<=str.length()<=20)
        for (char &c : str){
            if (islower(c)){
                c = toupper(c);
            }else if (isupper(c)){
                c = tolower(c);
            }
        }
    
    cout << str << endl;
        
    return 0;
}