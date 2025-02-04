#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int arr[100002];
int dp[100002][5][5];
int idx = 0;

int getVal(int from, int to) {
    if (from == to)
        return 1;
    else if (from == 0)
        return 2;
    else if (abs(from - to) % 2)
        return 3;
    return 4;
}

int main() {
    int n;
    while (true) {
        cin >> n;
        if (n == 0) break;
        arr[idx++] = n;
    }
    
    memset(dp, 0x3f, sizeof(dp)); // 큰 값으로 초기화
    dp[0][0][0] = 0;
    
    for (int depth = 0; depth < idx; ++depth) {
        int next = arr[depth];
        for (int left = 0; left < 5; ++left) {
            for (int right = 0; right < 5; ++right) {
                if (dp[depth][left][right] == 0x3f3f3f3f) continue; // 불가능한 상태 건너뛰기
                
                // 왼발을 움직이는 경우
                if (right != next) {
                    dp[depth + 1][next][right] = min(dp[depth + 1][next][right], dp[depth][left][right] + getVal(left, next));
                }
                
                // 오른발을 움직이는 경우
                if (left != next) {
                    dp[depth + 1][left][next] = min(dp[depth + 1][left][next], dp[depth][left][right] + getVal(right, next));
                }
            }
        }
    }
    
    int result = 0x3f3f3f3f;
    for (int left = 0; left < 5; ++left) {
        for (int right = 0; right < 5; ++right) {
            result = min(result, dp[idx][left][right]);
        }
    }
    
    cout << result << '\n';
    return 0;
}
