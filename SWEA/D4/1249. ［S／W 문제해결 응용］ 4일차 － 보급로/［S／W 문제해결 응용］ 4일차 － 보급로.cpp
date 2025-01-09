/*
출발지에서 도착지까지 가기 위한 도로 복구 작업 수행
도로가 파여진 깊이에 비례해서 복구 시간 증가
복구 시간이 가장 짧은 경로에 대한 총 복구시간을 구하기

상하좌우 이동 가능
지도 정보에는 각 칸마다 파여진 도로의 깊이가 주어짐

풀이 : 도로 복구 시간을 우선으로 판단하는 heap 사용
*/

#include <iostream>
#include <queue>
#include <string>

using namespace std;

int t, n;
int grid[101][101];
int visited[101][101];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

void init() {
	for (int i = 0; i < 101; i++) {
		for (int j = 0; j < 101; j++) {
			grid[i][j] = 0;
			visited[i][j] = 10001;
		}
	}
	cin >> n;
	for (int i = 0; i < n; i++) {
		string s; cin >> s;
		for (int j = 0; j < s.size(); j++)
			grid[i][j] = (int)s[j] - '0';
	}
}

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < n;
}

int bfs(int sr, int sc) {
	priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
	pq.push({ 0, {0, 0} });
	visited[sr][sc] = 0;

	while (!pq.empty()) {
		int move = pq.top().first;
		int r = pq.top().second.first, c = pq.top().second.second;
		pq.pop();

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc)) {
				if (visited[nr][nc] > visited[r][c] + grid[nr][nc]) {
					if (nr == n - 1 && nc == n - 1)
						return move;
					pq.push({ move + grid[nr][nc], {nr, nc} });
					visited[nr][nc] = visited[r][c] + grid[nr][nc];
				}
				
			}
		}
	}
	return -1;
}

int main() {
	cin >> t;
	for (int tc = 1; tc < t + 1; tc++) {
		init();
		
		int ans = bfs(0, 0);
		cout << '#' << tc << ' ' << ans << '\n';
	}


	return 0;
}