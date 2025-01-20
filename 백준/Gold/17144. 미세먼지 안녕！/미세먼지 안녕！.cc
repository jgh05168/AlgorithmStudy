/*
r x c
1초동안 아래 적힌 일이 순서대로 일어남
1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어남
	- r, c에 있는 미세먼지는 인접한 네 방향으로 확산된다.
	- 인접한 방향에 공기청정기 있거나 칸 없으면 확산 x
	- 확산되는 양은 /5이고 소수점은 버림
	- r, c에 남은 미세먼지 양은 a - a / 5 x 확산된 방향 수
2. 공기청정기 작동
	- 위쪽 공청기의 바람은 반시계, 아래쪽은 시계방향 순환
	- 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
	- 공청기로 들어간 미세먼지는 정화

풀이 : 구현
*/

#include <iostream>
#include <cstring>

using namespace std;

int n, m, t;
int grid[51][51];
int copy_grid[51][51];
pair<int, int> cleaner[2];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };


bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}


void spread_dusts() {
	memset(copy_grid, 0, sizeof(copy_grid));
	for (auto node : cleaner)
		grid[node.first][node.second] = -1;

	for (int r = 0; r < n; r++) {
		for (int c = 0; c < m; c++) {
			if (grid[r][c]) {
				int spread_cnt = 0;
				int div_dust = grid[r][c] / 5;
				for (int d = 0; d < 4; d++) {
					int nr = r + dr[d];
					int nc = c + dc[d];
					if (isValid(nr, nc) && grid[nr][nc] != -1) {
						copy_grid[nr][nc] += div_dust;
						spread_cnt++;
					}
				}
				copy_grid[r][c] += grid[r][c] - div_dust * spread_cnt;
			}	
		}
	}

	for (int r = 0; r < n; r++) {
		for (int c = 0; c < m; c++) 
			grid[r][c] = copy_grid[r][c];
	}
}

void rotate(int sr, int sc, int flag) {
	int d = 0;
	int nr, nc;

	int r = sr + dr[d];
	int c = sc + dc[d];
	int tmp = grid[r][c], next_tmp;
	while (grid[r][c] != -1) {
		nr = r + dr[d], nc = c + dc[d];
		if (!isValid(nr, nc)) {
			if (!flag)
				d = (d + 4 - 1) % 4;
			else
				d = (d + 1) % 4;
			nr = r + dr[d], nc = c + dc[d];
		}
		
		next_tmp = grid[nr][nc];
		grid[nr][nc] = tmp;
		tmp = next_tmp;
		
		r = nr;
		c = nc;
	}
	grid[sr][sc] = -1;
	grid[sr + dr[0]][sc + dc[0]] = 0;

}


void operate_cleaner() {
	int tmp;
	for (int i = 0; i < 2;i++) {
		int r = cleaner[i].first, c = cleaner[i].second;
		rotate(r, c, i);
	}
}


void init() {
	cin >> n >> m >> t;
	int tmp = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> grid[i][j];
			if (grid[i][j] == -1)
				cleaner[tmp++] = { i, j };
		}
	}
}


void solution() {
	while (t--) {
		// 1. 미세먼지 확산
		spread_dusts();

		// 2. 공기청정기 작동
		operate_cleaner();
	}

	int ans = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (grid[i][j] > 0)
				ans += grid[i][j];
		}
	}

	cout << ans << '\n';
}

int main() {
	init();

	solution();
	return 0;
}