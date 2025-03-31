/*
12:25 시작

등산로 N x N
1. 가장 높은 봉우리에서 시작한다
2. 높은 지형에서 낮은 지형으로 상하좌우 연결되야함
3. 긴 등산로를 위해  "딱 한 곳"을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.

풀이 : DFS
1. init에서 가장 높은 봉우리 찾기
2. 높은 봉우리 걸릴 때마다 DP 초기화 & DFS 진행
*/

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int t;
int n, k, ans = 0;
int max_height = 0, crash = 0;
int grid[9][9];
int visited[9][9];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}


void init() {
	ans = 0;
	max_height = 0;
	memset(grid, 0, sizeof(grid));

	cin >> n >> k;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> grid[i][j];
			max_height = max(max_height, grid[i][j]);
		}
	}
}


void DFS(int r, int c) {
	ans = max(ans, visited[r][c]);

	for (int d = 0; d < 4; d++) {
		int nr = r + dr[d], nc = c + dc[d];
		if (isValid(nr, nc) && !visited[nr][nc]) {
			if (grid[nr][nc] < grid[r][c]) {
				visited[nr][nc] = visited[r][c] + 1;
				DFS(nr, nc);
				visited[nr][nc] = 0;
			}
			else if (!crash) {
				crash = 1;
				int origin = grid[nr][nc];
				for (int power = 1; power < k + 1; power++) {
					grid[nr][nc]--;
					if (grid[nr][nc] < grid[r][c]) {
						visited[nr][nc] = visited[r][c] + 1;
						DFS(nr, nc);
						visited[nr][nc] = 0;
					}
				}
				grid[nr][nc] = origin;
				crash = 0;
			}
		}
	}
	
}


void simulation() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (max_height == grid[i][j]) {
				crash = 0;
				memset(visited, 0, sizeof(visited));
				visited[i][j] = 1;
				DFS(i, j);
			}
		}
	}
}


int main() {
	cin >> t;
	for (int tc = 1; tc < t + 1; tc++) {
		init();

		simulation();

		cout << '#' << tc << ' ' << ans << '\n';
	}

	return 0;
}