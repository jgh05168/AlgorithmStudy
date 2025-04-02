/*
11:30 시작

사냥꾼들은 나무 뒤에 숨어있다. 
하지만, 어떤 나무 뒤에 숨어있는지 알지 못한다.
현우의 목적지 : 숲의 한 오두막
현우는 나무와 거리가 최대한 떨어지는 경로로 대피하려 한다.

나무가 있는 칸으로도 이동이 가능함
현우와 나무의 거리는 맨해튼거리로 계산된다.
가장 안전한 길 : 현우가 이동하는 모든 칸에서 나무와 거리의 최솟값이 가장 큰 경로

나무의 개수는 여러개일 수 있음

풀이 : 
1. 초기에 빈 칸에서 나무까지의 최소 거리값을 저장해두는 grid 생성
	-> 나무 위치에 대해서 BFS 사용해서 각 칸마다 나무와의 최소 거리 구하기
	-> get_dist() 써서 일일이 계산하게 된다면 최악의 경우, 2500000 x 2500000 로 시간초과 발생함
2. 우선순위큐를 사용해서 이동하기
	-> 시간복잡도는 500 x 500 소요된다.
*/

#include <iostream>
#include <cstring>
#include <string>
#include <queue>
#include <algorithm>
#include <vector>

using namespace std;

int n, m;
char grid[501][501];
int min_dist[501][501] = { 0, };
int visited[501][501] = { 0, };
vector<pair<int, int>> tree_list;
int wolf_r, wolf_c, home_r, home_c;
int ans = 250000000;

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

bool isValid(int r, int c) {
	return 0 <= r && r < n && 0 <= c && c < m;
}

int get_dist(int r1, int c1, int r2, int c2) {
	return abs(r1 - r2) + abs(c1 - c2);
}


void calculate_min_dist() {
	queue<pair<int, int>> q;
	memset(min_dist, -1, sizeof(min_dist));

	// 모든 나무를 시작점으로 BFS 수행
	for (auto tree : tree_list) {
		int r = tree.first, c = tree.second;
		q.push({ r, c });
		min_dist[r][c] = 0;
	}

	while (!q.empty()) {
		int r = q.front().first, c = q.front().second;
		q.pop();

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && min_dist[nr][nc] == -1) {
				min_dist[nr][nc] = min_dist[r][c] + 1;
				q.push({ nr, nc });
			}
		}
	}
}


void init() {
	string tmp;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> tmp;
		for (int j = 0; j < m; j++) {
			grid[i][j] = tmp[j];
			if (grid[i][j] == 'V')
				wolf_r = i, wolf_c = j;
			if (grid[i][j] == 'J')
				home_r = i, home_c = j;
			if (grid[i][j] == '+')
				tree_list.push_back({ i, j });
		}
	}

	calculate_min_dist();
}


void bfs(int sr, int sc) {
	priority_queue<pair<int, pair<int, int>>> pq;
	pq.push({ min_dist[sr][sc], {sr, sc} });
	visited[sr][sc] = 1;

	while (!pq.empty()) {
		int cur_dist = pq.top().first;
		int r = pq.top().second.first, c = pq.top().second.second;
		pq.pop();

		ans = min(ans, cur_dist);

		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d], nc = c + dc[d];
			if (isValid(nr, nc) && !visited[nr][nc]) {
				if (grid[nr][nc] == 'J') {
					ans = min(ans, min_dist[nr][nc]);
					return;
				}
				visited[nr][nc] = 1;
				pq.push({ min_dist[nr][nc], {nr, nc} });
			}
		}
	}
}


int main() {
	init();

	bfs(wolf_r, wolf_c);

	cout << ans << '\n';

	return 0;
}