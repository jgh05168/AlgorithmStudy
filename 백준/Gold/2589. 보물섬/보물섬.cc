/*
쉽게 생각하면, 한 덩어리를 찾은 경우, bfs 돌려가며 최댓값 리턴하기
*/

#include <iostream>
#include <queue>
#include <algorithm>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
char grid[51][51];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool check_move(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c <= m;
}

int bfs(int sr, int sc) {
	int max_move = 0;
	int visited[51][51] = { 0, };
	queue<pair<int, int>> q;
	visited[sr][sc] = 1;
	q.push({ sr, sc });
	
	while (!q.empty()) {
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		max_move = max(max_move, visited[r][c] - 1);
		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];
			if (check_move(nr, nc) && !visited[nr][nc] && grid[nr][nc] == 'L') {
				visited[nr][nc] = visited[r][c] + 1;
				q.push({ nr, nc });
			}
		}
	}

	return max_move;
}

int main() {
	cin >> n >> m;
	int answer = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			cin >> grid[i][j];
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			if (grid[i][j] == 'L')
				answer = max(answer, bfs(i, j));
	}

	cout << answer << '\n';

	return 0;
}