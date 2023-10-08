#include <iostream>
using namespace std;

int main() {
    int N, originalN, cycleLength = 0;
    cin >> N;
    originalN = N;

    if (0 <= N && N <= 99) {
        do {
            int tens = N / 10;
            int units = N % 10;
            int sum = tens + units;
            N = units * 10 + sum % 10;
            cycleLength++;
        } while (N != originalN);

        cout << cycleLength << endl;
    } else {
        cout << "입력값은 0부터 99까지의 정수여야 합니다." << endl;
    }

    return 0;
}