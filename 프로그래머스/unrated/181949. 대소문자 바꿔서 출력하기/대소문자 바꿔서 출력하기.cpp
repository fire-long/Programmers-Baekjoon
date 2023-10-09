#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    if (1<=str.length()<=20)
        for (char &c : str){
            //&c는 참조하는 것으로, 변수에 대한 별칭임.
            if (islower(c)){
                c = toupper(c);
            }else if (isupper(c)){
                c = tolower(c);
            }
        }
    
    cout << str << endl;
        
    return 0;
}
