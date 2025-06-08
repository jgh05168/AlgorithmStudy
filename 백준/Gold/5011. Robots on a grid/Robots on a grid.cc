/*
오른쪽과 아래로만 이동가능한 로봇

1. 이동가능한 경로가 있는지 bfs로 체크
2. dp로 s -> t까지 경로가 몇 게 있는지 체크
*/

#include <iostream>
#include <cstring>
#include <string>
#include <queue>
using namespace std;

const long long MOD = (1LL << 31) - 1;

int n;
char grid[1001][1001];
long long dp[1001][1001];
bool visited_bfs[1001][1001];

int dr4[] = { 0, 1, 0, -1 };
int dc4[] = { 1, 0, -1, 0 };

int dr2[] = { 0, 1 };
int dc2[] = { 1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}

bool checkPathWithAllDirections() {
	if (n == 1) return true;

	memset(visited_bfs, 0, sizeof(visited_bfs));
	queue<pair<int, int>> q;

	q.push({ 0, 0 });
	visited_bfs[0][0] = true;

	while (!q.empty()) {
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		if (r == n - 1 && c == n - 1) {
			return true;
		}

		for (int i = 0; i < 4; i++) {
			int nr = r + dr4[i];
			int nc = c + dc4[i];

			if (isValid(nr, nc) && grid[nr][nc] == '.' && !visited_bfs[nr][nc]) {
				visited_bfs[nr][nc] = true;
				q.push({ nr, nc });
			}
		}
	}
	return false;
}

long long countPathsDownRight(int r, int c) {
	if (r == n - 1 && c == n - 1) {
		return 1;
	}
	if (!isValid(r, c) || grid[r][c] == '#') {
		return 0;
	}

	long long &ret = dp[r][c];
	if (ret != -1) {
		return ret;
	}

	ret = 0;
	ret = (ret + countPathsDownRight(r + dr2[0], c + dc2[0])) % MOD;
	ret = (ret + countPathsDownRight(r + dr2[1], c + dc2[1])) % MOD;

	return ret;
}

int main() {

	cin >> n; // 그리드 크기 입력

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> grid[i][j];
		}
	}

	memset(dp, -1, sizeof(dp));

	long long paths_down_right = countPathsDownRight(0, 0);

	if (paths_down_right > 0) {
		cout << paths_down_right << '\n';
	}
	else {
		bool path_exists_any_direction = checkPathWithAllDirections();

		if (path_exists_any_direction) {
			cout << "THE GAME IS A LIE" << '\n';
		}
		else {
			cout << "INCONCEIVABLE" << '\n';
		}
	}

	return 0;
}