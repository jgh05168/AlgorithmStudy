/*
n x m 크기의 건포도 초콜릿
하나의 건포도는 한 격자에만 속하고, 튀어나오지 않음

- 현수는 직사각형 전체를 일직선으로 자르는 행동만 가능함 -> 보상 요구
돈 대신 건포도를 지불
초콜릿 한 조각을 작은 두 조각으로 자를 떄마다, 초기 큰 초콜릿에 있었던 건포도의 개수만큼 받는다.
지불해야하는 건포도의 최소 양을 구하여라

풀이 : 
1. 일단 완전탐색 + 재귀함수로 접근하자.
	-> 시간초과난다.
2. 메모이제이션 사용한 DP로 풀이
	-> DP 테이블은 4차원으로 가져가기 : dp[a][b][c][d] ==> a : 시작 r, b : 시작 c, c : 종료 r, d : 종료 c
+ 중복 구간 계산을 방지하기 위해 누적합으로 건포도 개수를 구해놓자


*/

#include <iostream>
#include <algorithm>
#include <cstring>
#define INF 2e9

using namespace std;

int t, n, m;
int dp[51][51][51][51];
int chocolate[51][51];
int prefix_sum[51][51];

void calcSum() {
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < m + 1; j++)
			prefix_sum[i][j] = chocolate[i][j] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1];
	}
}


int recur(int sr, int sc, int er, int ec) {
	// 종료 조건
	if (sr == er && sc == ec)
		return 0;
	// 메모이제이션 조건
	if (dp[sr][sc][er][ec] != -1)
		return dp[sr][sc][er][ec];

	int duplicate_sum = prefix_sum[er][ec] - prefix_sum[sr - 1][ec] - prefix_sum[er][sc - 1] + prefix_sum[sr - 1][sc - 1];
	dp[sr][sc][er][ec] = INF;
	// 가로로 자르기
	for (int i = sr; i < er; i++) {
		dp[sr][sc][er][ec] = min(dp[sr][sc][er][ec], recur(sr, sc, i, ec) + recur(i + 1, sc, er, ec) + duplicate_sum);
	}
	// 세로로 자르기
	for (int i = sc; i < ec; i++) {
		dp[sr][sc][er][ec] = min(dp[sr][sc][er][ec], recur(sr, sc, er, i) + recur(sr, i + 1, er, ec) + duplicate_sum);
	}

	return dp[sr][sc][er][ec];
}


int main() {
	cin >> t;
	for (int tc = 1; tc < t + 1; tc++) {
		cin >> n >> m;
		memset(prefix_sum, 0, sizeof(prefix_sum));
		memset(dp, -1, sizeof(dp));
		for (int i = 1; i < n + 1; i++) {
			for (int j = 1; j < m + 1; j++)
				cin >> chocolate[i][j];
		}
		// 누적합 진행
		calcSum();

		// dp 시작
		int ans = recur(1, 1, n, m);

		cout << '#' << tc << ' ' << ans << '\n';

	}
	return 0;
}