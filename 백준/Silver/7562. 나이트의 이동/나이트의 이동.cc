/*
visited 배열 필요
범위 벗어나면 종료
미리 dx, dy 배열 작성
*/

#include <iostream>
#include <queue>

using namespace std;

int dr[8] = { 1, 2, 2, 1, -1, -2, -2, -1 };
int dc[8] = { 2, 1, -1, -2, -2, -1, 1, 2 };


int bfs(pair<int, int> s, pair<int, int> e, int l) {
	queue<pair<int, int>> q;
	q.push(s);
	int visited[301][301] = { 0, };
	visited[s.first][s.second] = 1;
	int r, c, nr, nc;

	while (!q.empty()) {
		r = q.front().first;
		c = q.front().second;
		q.pop();

		for (int d = 0; d < 8; d++) {
			nr = r + dr[d];
			nc = c + dc[d];
			if (0 <= nr && nr < l && 0 <= nc && nc < l && visited[nr][nc] == 0) {
				if (nr == e.first && nc == e.second) {
					return visited[r][c];
				}
				else {
					q.push({ nr, nc });
					visited[nr][nc] = visited[r][c] + 1;
				}
			}
		}
	}

	return -1;
}


int main() {
	int t;
	cin >> t;
	for (int tc = 0; tc < t; tc++) {
		int l;
		pair<int, int> s, e;
		
		cin >> l;
		cin >> s.first >> s.second;
		cin >> e.first >> e.second;

		if (s == e) {
			cout << 0 << '\n';
		}
		else {
			cout << bfs(s, e, l) << '\n';
		}


	}

	return 0;
}