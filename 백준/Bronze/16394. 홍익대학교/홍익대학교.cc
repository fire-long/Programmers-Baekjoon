#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int start = 1946;
    int N;
    cin>>N;
    if (1946<=N<=1000000)
        cout << N-start;
    return 0;
}