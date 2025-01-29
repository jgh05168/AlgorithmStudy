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

int dp[11][11];
unordered_map<string, int> string_table;

int dr[8] = { 0, 1, 1, 1, 0, -1, -1, -1 };
int dc[8] = { 1, 1, 0, -1, -1, -1, 0, 1 };


int top_down(int depth, string cur_s, int r, int c) {
	// 종료 조건
	if (depth == s_size) {
		if (cur_s == s)
			return 1;
		return 0;
	}

	// 해당 칸에 방문한 경우가 존재하면 return
	if (dp[r][c] != -1)
		return dp[r][c];

	// 8방향 탐색 시작
	int dp_val = 0;
	for (int d = 0; d < 8; d++) {
		int nr = (r + dr[d] + n) % n;
		int nc = (c + dc[d] + m) % m;
		if (grid[nr][nc] == s[depth])
			dp_val += top_down(depth + 1, cur_s + grid[nr][nc], nr, nc);
	}
	return dp_val;
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
		int answer = 0;
		cin >> s;
		// 이전에 중복된 값이면 바로 출력
		if (string_table[s]) {
			cout << string_table[s] << '\n';
			continue;
		}
		// 경우의 수 탐색 시작
		s_size = s.size();
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (grid[i][j] == s[0]) {
					memset(dp, -1, sizeof(dp));
					string new_s = "";
					answer += top_down(1, new_s + grid[i][j], i, j);
				}
			}
		}
		cout << answer << '\n';
		string_table[s] = answer;
	}

}


int main() {
	init();

	solution();

	return 0;
}