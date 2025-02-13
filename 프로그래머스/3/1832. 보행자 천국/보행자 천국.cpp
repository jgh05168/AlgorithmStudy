/*
도심의 일부 구역은 자동차 통행이 금지, 일부 교차로에서는 좌우회전 금지
1: 자동차 통행 금지
2: 직진만 가능
도로 상태가 입력으로 주어졌을 때, 이동가능한 전체 가능 경로 수를 출력하자
가능한 경로 수를 20170805로 나눈 나머지값을 출력

풀이 : DFS + DP
메모이제이션 방식을 사용한다.
경로 이동은 동일하게 활용하기

grid[r][c] 가 2인 경우는 따로 조건문 걸어주기
*/


#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int MOD = 20170805;

int N, M;
int grid[501][501] = { 0, };
int dp[501][501][2];

int dr[2] = { 0, 1 };
int dc[2] = { 1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < N && 0 <= c && c < M;
}

int dfs(int r, int c, int d) {
	if (r == N - 1 && c == M - 1)
		return 1;
	if (grid[r][c] == 1)
		return 0;
	if (dp[r][c][d] != -1)
		return dp[r][c][d];
	int nr, nc;
	int tmp = 0;
	// 직진만 가능한 경우
	if (grid[r][c] == 2) {
		nr = r + dr[d], nc = c + dc[d];
		if (isValid(nr, nc)) {
			tmp += (dfs(nr, nc, d) % MOD);
		}
	}
	else {
		for (int nd = 0; nd < 2; nd++) {
			nr = r + dr[nd], nc = c + dc[nd];
			if (isValid(nr, nc)) {
				tmp += (dfs(nr, nc, nd) % MOD);
			}
		}
	}
	dp[r][c][d] = tmp % MOD;
	// cout << r << ' ' << c << ' ' << dp[r][c][d]<< '\n';
	return dp[r][c][d];
}


// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int m, int n, vector<vector<int>> city_map) {
	int answer = 0;
	N = m, M = n;
	memset(dp, -1, sizeof(dp));
	for (int i = 0; i < m; i++) {
		for (int j = 0; j < n; j++)
			grid[i][j] = city_map[i][j];
	}

	answer = dfs(0, 0, 0);

	return answer;
}
