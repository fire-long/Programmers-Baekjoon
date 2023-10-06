#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<vector<char>> room(N, vector<char>(N));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> room[i][j];
        }
    }

    int horizontal_count = 0;
    int vertical_count = 0;

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
                empty_count = 0;
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