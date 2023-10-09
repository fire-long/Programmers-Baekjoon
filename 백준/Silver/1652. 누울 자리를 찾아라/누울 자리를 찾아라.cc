#include <iostream>
#include <vector>

using namespace std;
// 사용자로부터 정사각형 방의 크기(N)와 각 위치의 상태를 입력받아, 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 수를 세는 프로그램
int main() {
    int N;
    cin >> N;

    vector<vector<char>> room(N, vector<char>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> room[i][j];
        }
    }

    int horizontal_count = 0; // 가로로 누울 수 있는 자리의 수
    int vertical_count = 0; //세로로 누울 수 있는 자리의 수

    // 가로로 누울 수 있는 자리 검사
    for (int i = 0; i < N; ++i) {
        int empty_count = 0;
        for (int j = 0; j < N; ++j) {
            if (room[i][j] == '.') {
                empty_count++;
            } else {
                if (empty_count >= 2) {
                    horizontal_count++;
                }
                empty_count = 0; //빈자리가 아닌 다른 문자가 나타날 때 0으로 초기화
            }
        }
        if (empty_count >= 2) {
            horizontal_count++;
        }
    }

    // 세로로 누울 수 있는 자리 검사
    for (int j = 0; j < N; ++j) {
        int empty_count = 0;
        for (int i = 0; i < N; ++i) {
            if (room[i][j] == '.') {
                empty_count++;
            } else {
                if (empty_count >= 2) {
                    vertical_count++;
                }
                empty_count = 0;
            }
        }
        if (empty_count >= 2) {
            vertical_count++;
        }
    }

    cout << horizontal_count << " " << vertical_count << endl;

    return 0;
}
