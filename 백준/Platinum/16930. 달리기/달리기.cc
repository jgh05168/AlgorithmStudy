/*
12:50

달리기

해당 방향으로 최소 1칸, 최대 K개의 빈 칸을 이동한다.
출발지부터 목적지까지 갈 수 있는 최소 시간을 구하자.

visited에 최소 시간을 계산해두기. 
근데, 1000 x 1000에다가 시간별로 계산을 하면 x1000을 더 해야함 == 시간초과.

-> path 딴 다음, 한 칸씩 이동하면서 경로 업데이트하기 ??
	해 보 자 .
-------- 실 패 ----------
bfs로 모든 조건에 대해 탐색은 해보되, 가지치기를 하자.
queue에 삽입할 때, 가지치기를 진행 : 큐에 담겨져 있는 같은 거리의 큐를 한꺼번에 탐색해보자.
	-> 거리별로 탐색을 진행할 것이기 때문에, 가지치기가 될 것임
*/
#include <iostream>
#include <cstring>
#include <queue>
#define INF 99999999
using namespace std;

int n, m, k;
int sr, sc, er, ec;
char grid[1001][1001];
int visited[1001][1001];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}

void init() {
	cin.tie(0);
	ios::sync_with_stdio(false);
	cin >> n >> m >> k;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> grid[i][j];
			visited[i][j] = INF;
		}
	}
	cin >> sr >> sc >> er >> ec;
	sr--, er--, sc--, ec--;
}

int bfs() {
	queue<pair<int, int>> q;
	q.push({ sr, sc });
	visited[sr][sc] = 0;

	while (!q.empty()) {
		int r = q.front().first;
		int c = q.front().second;
		q.pop();

		if (r == er && c == ec) {
			return visited[r][c];
		}

		for (int d = 0; d < 4; d++) {
			for (int move = 1; move <= k; move++) {
				int nr = r + dr[d] * move;
				int nc = c + dc[d] * move;

				// 현재 위치가 새로운 이동보다 작다면, continue 해줘야함
				// visited는 다익스트라의 cost처럼 활용
				if (!isValid(nr, nc) || grid[nr][nc] == '#' || visited[nr][nc] < visited[r][c] + 1) 
					break;

				if (visited[nr][nc] == INF) {
					visited[nr][nc] = visited[r][c] + 1;
					q.push({ nr, nc });
				}
			}
			
		}
	}
	return -1;
}

int main() {
	init();
	cout << bfs() << '\n';
	return 0;
}