/*
해야할 일이 총 n개
최대한 늦게 일을 시작할 수 있는 시간을 찾자
일하는데 걸리는 시간, 마감기한 주어짐

풀이 : 정렬, 그리디
*/

#include <iostream>
#include <queue>
#include <string>

using namespace std;

int n, m;
int ans = -1;
int chk = 0;
string grid[3002];
int visited[3002][3002];

int dr[4] = { -1, 0, 1, 0 };
int dc[4] = { 0, -1, 0, 1 };

queue<pair<int, int>> q;

void init() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> grid[i];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			visited[i][j] = -1;
			if (grid[i][j] == '2') {
				q.push({ i, j });
				visited[i][j] = 0;
			}
		}
	}
}


void solution() {
	while (!q.empty()) {
		int r = q.front().first, c = q.front().second;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];

			if (nr < 0 || nc < 0 || nr >= n || nc >= m) 
				continue;
			if (grid[nr][nc] == '1' || visited[nr][nc] != -1) 
				continue;

			// 종료 조건
			if (grid[nr][nc] == '3' || grid[nr][nc] == '4' || grid[nr][nc] == '5') {
				ans = visited[r][c] + 1;
				chk = 1;
				return;
			}

			q.push({ nr, nc });
			visited[nr][nc] = visited[r][c] + 1;
		}
	}
}

int main() {
	init();

	solution();

	if (ans == -1) {
		cout << "NIE" << '\n';
	}
	else {
		cout << "TAK" << '\n' << ans << '\n';
	}

	return 0;
}
