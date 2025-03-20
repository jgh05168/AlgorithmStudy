/*
n x m, 상하좌우 움직이고 0이 적힌 방 못들어감
1. 두 방 사이의 최단경로로 이동한다.
2. 1번을 만족하는 경로 중 가장 긴 경로의 시작방과 끝 방 숫자의 합

풀이 : 모든 방 돌면서 bfs 진행, 전역변수로 방 길이 체크
*/

#include <iostream>
#include <cstring>
#include <queue>
#include <algorithm>

using namespace std;

int n, m;
int max_dist = 0, ans = 0;
int grid[51][51];
int visited[51][51];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };


bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}

void bfs(int sr, int sc) {
	queue<pair<int, int>> q;
	q.push({ sr, sc });
	memset(visited, -1, sizeof(visited));
	visited[sr][sc] = 1;
	int start_pw = grid[sr][sc];

	while (!q.empty()) {
		int r = q.front().first, c = q.front().second;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && visited[nr][nc] == -1 && grid[nr][nc]) {
				q.push({ nr, nc });
				visited[nr][nc] = visited[r][c] + 1;
				// 최대 길이 체크
				if (visited[nr][nc] > max_dist) {
					max_dist = visited[nr][nc];
					ans = start_pw + grid[nr][nc];
				}
				else if (visited[nr][nc] == max_dist)
					ans = max(ans, start_pw + grid[nr][nc]);
			}
		}
	}
}


void init() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cin >> grid[i][j];
	}
}


void solution() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (grid[i][j]) {
				bfs(i, j);
			}
		}
			
	}
}


int main() {
	init();

	solution();

	cout << ans << '\n';

	return 0;
}