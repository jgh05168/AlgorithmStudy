/*
집이 n개 존재 1 ~ n
각각의 집을 R, G, B로 칠하는 비용이 주어졌을 때, 규칙을 만족하며 모든 집을 칠하는 최솟값 출력
- 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다
- N번 집의 색은 N - 1, 1번 집의 색과 같지 않아야 한다
- i번 집의 색은 i - 1, i + 1번 집의 색과 같지 않아야한다

N <= 1000
풀이 : 
- 3번 각각 진행시켜주어 최솟값 찾기
O(3 x 1000)
*/

#include <iostream>
#include <algorithm>
#include <vector>
#define INIT cin.tie(0); ios::sync_with_stdio(false);
#define INF 1000000;

using namespace std;

int n;
int a, b, c;
int grid[1001][3];
int dp[1001][3];
int ans = INF;

int main() {
	INIT;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> a >> b >> c;
		grid[i][0] = a; grid[i][1] = b; grid[i][2] = c;
	}

	// dp 시작 ( 각 구간별로 )
	for (int rgb = 0; rgb < 3; rgb++) {
		for (int i = 0; i < 3; i++) {
			if (rgb == i) dp[0][i] = grid[0][i];
			else dp[0][i] = INF;
		}
		for (int i = 1; i < n; i++) {
			dp[i][0] = grid[i][0] + min(dp[i - 1][1], dp[i - 1][2]);
			dp[i][1] = grid[i][1] + min(dp[i - 1][0], dp[i - 1][2]);
			dp[i][2] = grid[i][2] + min(dp[i - 1][1], dp[i - 1][0]);
		}
		// 1열과 n열이 같은지 체크(같으면 continue)
		for (int i = 0; i < 3; i++) {
			if (rgb == i) continue;
			ans = min(ans, dp[n - 1][i]);
		}
	}

	cout << ans << '\n';

	return 0;
}