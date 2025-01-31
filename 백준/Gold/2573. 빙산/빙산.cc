/*
빙산

바닷물과 접해있는 면 만큼 줄어든다.
빙산이 두 덩어리 이상으로 분리되는 최초의 시간을 구하기
전부 다 녹을 때까지 분리되지 않으면 0 출력

풀이 : 빙산 가장자리 저장
시간 지난 뒤 전체에 대해 bfs
*/

#include <iostream>
#include <queue>
#include <iostream>
#include <cstring>

using namespace std;

int n, m;
int grid[301][301];
int visited[301][301];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };


bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}


void bfs(int sr, int sc) {
	queue<pair<int, int>> q;
	q.push({ sr, sc });
	visited[sr][sc] = 1;

	while (!q.empty()) {
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && !visited[nr][nc] && grid[nr][nc]) {
				q.push({ nr, nc });
				visited[nr][nc] = 1;
			}
		}
	}
}


void check_side() {
	int new_grid[301][301] = { 0, };

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			new_grid[i][j] = grid[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (grid[i][j]) {
				int melt = 0;
				for (int d = 0; d < 4; d++) {
					int ni = i + dr[d], nj = j + dc[d];
					if (isValid(ni, nj) && !grid[ni][nj])
						melt++;
				}
				new_grid[i][j] -= melt;
				if (new_grid[i][j] <= 0) 
					new_grid[i][j] = 0;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			grid[i][j] = new_grid[i][j];
		}
	}
}


void init() {
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cin >> grid[i][j];
	}
}


int solution() {
	int answer = 0;

	while (1) {
		
		// 겹치는 빙산 찾기
		int separate = 0;
		int endflag = 1;
		memset(visited, 0, sizeof(visited));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (!visited[i][j] && grid[i][j]) {
					if (separate)
						return answer;
					bfs(i, j);
					separate = 1;
					endflag = 0;
				}
			}
		}
		if (endflag)
			return 0;
		answer++;

		// 빙산 가장자리 체크
		check_side();

	}
	return answer;
}


int main() {
	init();
	cout << solution() << '\n';
	return 0;
}