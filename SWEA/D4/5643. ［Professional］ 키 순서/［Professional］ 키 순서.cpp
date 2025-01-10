/*
n명의 키는 모두 다르다
a번 학생의 키가 b번 학생의 키보다 작다면, a에서 b로 화살표를 그려서 표현하였다.

자신의 키가 몇 번째인지 알 수 있는 학생들이 모두 몇 명일까?

풀이 : 
양방향 그래프 순회하면서 방문 횟수가 n - 1이라면 정확히 자신의 키를 알 수 있는 상태다.
bfs 대신 dfs 사용
*/

#include <iostream>
#include <cstring>

using namespace std;

int t, n, m;
int to_tall[501][501];
int to_small[501][501];
int visited[501];
int cnt[501];


void dfs(int graph[501][501], int u) {
	visited[u] = 1;
	for (int v = 1; v < n + 1; v++) {
		if (!visited[v] && graph[u][v]) {
			dfs(graph, v);
			cnt[v]++;
		}
	}
}


int main() {
	cin >> t;
	for (int tc = 1; tc < t + 1; tc++) {
		// input()
		memset(to_tall, 0, sizeof(to_tall));
		memset(to_small, 0, sizeof(to_small));
		memset(cnt, 0, sizeof(cnt));
		cin >> n >> m;
		int a, b;
		for (int i = 0; i < m; i++) {
			cin >> a >> b;
			to_tall[a][b] = 1;
			to_small[b][a] = 1;
		}

		// start()
		for (int i = 1; i < n + 1; i++) {
			memset(visited, 0, sizeof(visited));
			dfs(to_tall, i);

			memset(visited, 0, sizeof(visited));
			dfs(to_small, i);
		}

		int ans = 0;
		for (auto total : cnt) {
			if (total == n - 1)
				ans++;
		}
		cout << '#' << tc << ' ' << ans << '\n';
	}

	return 0;
}


