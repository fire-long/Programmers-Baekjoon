#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false); //C++의 입출력 버퍼와 C 표준 입출력 버퍼를 동기화하지 않도록 설정 -> 성능저하 방지
    cin.tie(NULL); //cin과 cout의 동기화 기능 해제. cin은 입력 요청 시 자동으로 출력버퍼를 비워주는데 이때문에 성능 저하가 될 수 있기 때문.
    //독립적으로 동작시켜서 성능 향상
    
    int start = 1946;
    int N;
    cin>>N;
    if (1946<=N<=1000000)
        cout << N-start;
    return 0;
}
