/*
1, 2, 3의 합으로 나타내는 방법을 찾자

풀이 : dp
dp 배열은 10000 * 3 으로 구현
각 경우마다 dp 리턴
*/

#include <iostream>
#include <cstring>

using namespace std;

int t, n;
int dp[10001][4];


int topDown(int val, int idx) {
	if (val == 0)
		return 1;
	if (dp[val][idx] != -1)
		return dp[val][idx];

	int cnt = 0;
	for (int i = idx; i < 4; i++) {
		if (val - i >= 0) {
			cnt += topDown(val - i, i);
		}
	}

	dp[val][idx] = cnt;
	return cnt;
}


int main() {
	cin >> t;
	while (t--) {
		cin >> n;
		memset(dp, -1, sizeof(dp));

		cout << topDown(n, 1) << "\n";
	}

	return 0;
}
