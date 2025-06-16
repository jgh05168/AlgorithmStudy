/*
n x m, b개의 건물
건물에는 바이러스 살포를 못 함

1. 모든 바이러이러스는 살포 시점으로부터 t시간 뒤 전파를 멈춘다.
2. 비안전구역 & 상하좌우로 인접한 구역은 1시간 뒤 전파 완료된다.
	- 전파 완료 전까지 인접한 구역은 전파되지 않은 구역으로 간주
3. 바이러스가 전파된 시점으로부터 t시간 동안은 건물 내부에 바이러스가 퍼진다.
	- 이 기간동안 건물 내부는 전파되지 않은 층으로 대피가능
	- 건물이 더이상 안전하ㅣㅈ 않게 되면 마찬가지로 2번과 같이 바이러스가 전파된다.

하나의 구역은 격자 한 칸.

1000 x 1000
전파 지연 시간 <= 2000 이기 때문에 우선순위큐 사용하기
*/

#include <iostream>
#include <cstring>
#include <string>
#include <queue>

using namespace std;

struct node {
	int t, r, c;

	bool operator>(const node& other) const {
		return t > other.t;
	}
};

int n, m;
int Tg, Tb, x, b;

char grid[1001][1001];
int visited[1001][1001];
int safe_ing[1001][1001];

priority_queue<node, vector<node>, greater<node>> pq;

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}


void init() {
	string tmp;
	memset(visited, 0, sizeof(visited));
	memset(safe_ing, 0, sizeof(safe_ing));

	cin >> n >> m;
	cin >> Tg >> Tb >> x >> b;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		for (int j = 0; j < m; j++) {
			grid[i][j] = tmp[j];
			if (grid[i][j] == '*') {
				pq.push({ 0, i, j });
				visited[i][j] = 1;
			}
		}
	}

}


void simulation() {
	while (!pq.empty()) {
		int cur_t = pq.top().t;
		int r = pq.top().r, c = pq.top().c;
		pq.pop();

		if (safe_ing[r][c] && cur_t <= Tg) {
			safe_ing[r][c] = 0;
			visited[r][c] = 1;
		}

		if (cur_t >= Tg)
			continue;

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && !visited[nr][nc]) {
				if (grid[nr][nc] == '#') {
					if (safe_ing[nr][nc])
						continue;
					pq.push({ cur_t + Tb + 1, nr, nc });
					safe_ing[nr][nc] = 1;
				}
				else {
					pq.push({ cur_t + 1, nr, nc });
					visited[nr][nc] = 1;
				}
			}
		}
	}

	int flag = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!visited[i][j]) {
				cout << i + 1 << ' ' << j + 1 << '\n';
				flag = 1;
			}
		}
	}

	if (!flag)
		cout << -1 << '\n';
}

int main() {
	init();

	simulation();
}