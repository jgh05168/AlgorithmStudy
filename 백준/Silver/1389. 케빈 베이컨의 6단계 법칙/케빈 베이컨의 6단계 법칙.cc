/*
1389. 케빈 베이컨의 6단계 법칙

임의의 두 사람이 최소 몇 단계 만에 이어질 수 있는지 계산하는 게임
단계의 총 합이 가장 적은 사람

케빈 베이컨의 수가 가장 작은 사람을 구하자

풀이:
한 녀석이 모든 정점에 도달하는 데 걸리는 가중치의 총 합을 구하는 문제
M <= 5000, n <= 100

1. 중복 입력의 경우가 있기 때문에, 모든 사람 정보를 2차원 배열 형식으로 저장
2. 입력에서 모든 친구는 연결되어있다. 
3. bfs 탐색 진행
정답 출력의 경우 가장 작은 수의 사람을 업데이트 하는 방식으로 진행
*/

#include <iostream>
#include <queue>
#include<cstring>
#define INIT cin.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
int s, e;
int relationship[101][101] = { 0, };
int visited[101] = { 0, };

int ans = 0;
int max_r = 1000000;

void bfs(int su) {
	queue<int> q;
	memset(visited, 0, 101 * sizeof(int));
	q.push(su);
	visited[su] = 1;
	int tmp_r = 0;

	while (!q.empty()) {
		int u = q.front();
		q.pop();

		tmp_r += visited[u] - 1;
		if (tmp_r >= max_r)
			return;

		for (int v = 1; v <= n; v++) {
			if (relationship[u][v] && !visited[v]) {
				visited[v] = visited[u] + 1;
				q.push(v);
			}
		}
	}

	// 케빈 베이컨 수 계산
	if (tmp_r < max_r) {
		ans = su;
		max_r = tmp_r;
	}
}

int main() {
	INIT;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		cin >> s >> e;
		relationship[s][e] = 1;
		relationship[e][s] = 1;
	}

	// 1번부터 순회하며 bfs 진행
	for (int i = 1; i < n + 1; i++) {
		bfs(i);
	}

	cout << ans << '\n';

	return 0;
}