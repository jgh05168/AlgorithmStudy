/*
N개의 노드로 이루어진 트리
M개의 두 노드 쌍을 입력받을 때, 두 노드 사이의 거리 출력

풀이:
bfs, 입력 들어올 때마다 bfs 돌려서 찾기
*/

#include <iostream>
#include <queue>
#include <vector>
#include <cstring>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n, m;
int u, v, w;
int visited[1001] = { 0, };


int bfs(int su, int end, vector<vector<pair<int, int>>> graph) {
	queue<pair<int, int>> q;
	visited[su] = 1;
	q.push({ su, 0 });

	while (!q.empty()) {
		u = q.front().first;
		w = q.front().second;
		q.pop();

		for (int i = 0; i < graph[u].size(); i++) {
			v = graph[u][i].first;
			int nw = graph[u][i].second;
			if (!visited[v]) {
				if (v == end)
					return w + nw;
				visited[v] = 1;
				q.push({ v, w + nw });
			}
		}
	}

	return -1;

}

int main() {
	cin >> n >> m;
	vector<vector<pair<int, int>>> graph(n + 1);
	for (int i = 0; i < n - 1; i++) {
		cin >> u >> v >> w;
		graph[u].push_back({ v, w });
		graph[v].push_back({ u, w });
	}

	int start, end;
	while(m--) {
		cin >> start >> end;
		memset(visited, 0, 1001 * sizeof(int));
		cout << bfs(start, end, graph) << '\n';

	}

	return 0;
}