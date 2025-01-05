/*
c로 표시되어 있는 두 칸을 레이저로 통신하기 위해 설치해야 하는 거울 개수의 최솟값 구하기
레이저는 c에서만 발사 가능
빈 칸에 거울을 설치해서 방향을 90도 바꿀 수 있음

풀이 : 
bfs 진행
bfs 진행할 때, 현재 방향과 꺾인다면 값 1 증가시키기
설치된 거울의 개수를 첫번째 값으로 하여 우선순위큐 사용하기
*/

#include <iostream>
#include <queue>
#include <vector>
#include <map>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
char grid[101][101];
int visited[101][101] = { 0, };
map<pair<int, int>, int> q_available;

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

struct node {
	int mirror, row, col, dir;
};


bool checkMove(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}


struct cmp {
	bool operator()(node a, node b) {
		if (a.mirror == b.mirror) 
			return a.row < b.row;
		return a.mirror > b.mirror;
	}
};


int bfs(int sr, int sc) {
	priority_queue<node, vector<node>, cmp> q;
	q.push({ -1, sr, sc, -1 });
	visited[sr][sc] = -1;
	int ans = 1000001;

	while (!q.empty()) {
		int cnt = q.top().mirror;
		int r = q.top().row;
		int c = q.top().col;
		int direction = q.top().dir;
		q.pop();
		q_available[{r, c}]--;

		if (cnt >= ans)
			continue;
		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];
			if (checkMove(nr, nc)) {
				// 거울 설치 여부 확인
				int new_cnt = cnt;
				if (d != direction)
					new_cnt += 1;
				// 이동 가능 여부 확인
				if (visited[nr][nc] >= new_cnt && grid[nr][nc] != '*') {
					// 도착지인 경우
					if (grid[nr][nc] == 'C') {
						ans = min(ans, new_cnt);
					}
					// 도착지가 아닌 경우
					else {
						if (q_available[{nr, nc}] < 3) {
							q.push({ new_cnt, nr, nc, d });
							visited[nr][nc] = new_cnt;
							q_available[{nr, nc}]++;
						}
					}
				}
			}
		}
	}

	return ans;
}


int main() {
	INIT;
	cin >> m >> n;
	int sr = -1, sc = -1;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> grid[i][j];
			if (grid[i][j] == 'C' && sr == -1 && sc == -1) {
				sr = i;
				sc = j;
				grid[i][j] = '.';
			}
			visited[i][j] = 100001;
		}
	}

	int answer = bfs(sr, sc);

	cout << answer << '\n';

	return 0;
}