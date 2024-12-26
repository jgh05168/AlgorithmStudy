#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int dp[1000001] = { 0, };
int path[1000001] = { 0, };

int main() {
	cin >> n;

	dp[1] = 0; // 초기값 설정: 1을 1로 만드는 데 필요한 연산은 0회
	for (int i = 2; i <= n; i++) {
		dp[i] = dp[i - 1] + 1; // 기본 연산: 1을 빼는 경우
		path[i] = i - 1;       // 경로 저장

		if (i % 2 == 0 && dp[i] > dp[i / 2] + 1) {
			dp[i] = dp[i / 2] + 1; // 2로 나누는 경우
			path[i] = i / 2;       // 경로 저장
		}

		if (i % 3 == 0 && dp[i] > dp[i / 3] + 1) {
			dp[i] = dp[i / 3] + 1; // 3으로 나누는 경우
			path[i] = i / 3;       // 경로 저장
		}
	}

	cout << dp[n] << '\n'; // 최소 연산 횟수 출력

	// 경로 출력
	int move = n;
	while (move > 0) {
		cout << move << ' ';
		move = path[move];
	}
	return 0;
}
