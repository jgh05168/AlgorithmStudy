/*
헉 !

n행 m열, 각 칸에 알파벳 써있고 환형으로 이어짐
상하좌우 대각선 한 칸 이동 가능
	- 이미 지난 칸 다시 방문 가능
각 칸에 써진 알파벳을 이어붙여 문자열 만들기 가능
-문자열 k개 알려줄테니 너가 만들 수 있는 경우의 수를 잘 대답해야함
- 방문 순서가 다르면 다른 경우이다.

3 ≤ N, M ≤ 10
1 ≤ K ≤ 1,000
1 ≤ 문자열의 길이 ≤ 5
문자열 중복 가능 -> 해시로 값 저장해서 있는 값이면 출력

풀이 : depth는 총 5번 가능함 -> 깊지 않다. dfs 가능
모든 경우에 대해 살펴봐야 함 -> 시간초과임
	- 최적화 필요
경우의 수를 세는 경우니까 top-down dp 가능할지도 ?
	- 모든 경우에 대해 탑다운 적용하기 -> 1000 * 100 = 10만
*/

#include <iostream>
#include <string>
#include <cstring>
#include <unordered_map>

using namespace std;

int n, m, k, s_size;
char grid[11][11];
string s;
int dp[11][11][6]; // 최대 길이 5까지 저장 가능
unordered_map<string, int> string_table;

int dr[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int dc[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };

int top_down(int r, int c, int depth) {
	// 종료 조건 : 문자열이 맞는지는 사전에 검사했기 때문에 길이만 검사하면 된다.
	if (depth == s_size) 
		return 1;

	// DP 캐싱 확인
	if (dp[r][c][depth] != -1) 
		return dp[r][c][depth];

	dp[r][c][depth] = 0;

	// 8방향 탐색
	for (int d = 0; d < 8; d++) {
		int nr = (r + dr[d] + n) % n;
		int nc = (c + dc[d] + m) % m;
		if (grid[nr][nc] == s[depth]) {
			dp[r][c][depth] += top_down(nr, nc, depth + 1);
		}
	}
	return dp[r][c][depth];
}

void init() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		cin >> s;
		for (int j = 0; j < m; j++)
			grid[i][j] = s[j];
	}
}

void solution() {
	while (k--) {
		cin >> s;

		// 이미 계산한 문자열이면 바로 출력
		if (string_table.count(s)) {
			cout << string_table[s] << '\n';
			continue;
		}

		s_size = s.size();
		memset(dp, -1, sizeof(dp)); // DP 배열 초기화
		int answer = 0;

		// 모든 시작 위치 탐색
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (grid[i][j] == s[0]) {
					answer += top_down(i, j, 1);
				}
			}
		}

		cout << answer << '\n';
		string_table[s] = answer; // 결과 캐싱
	}
}

int main() {
	init();
	solution();
	return 0;
}
