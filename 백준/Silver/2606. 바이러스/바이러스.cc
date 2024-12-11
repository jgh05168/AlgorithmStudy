#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int n, m;
int u, v;
int visited[101] = { 0, };

void bfs(int su, vector<vector<int>> graph) {
	queue<int> q;
	q.push(su);
	visited[su] = 1;

	while (!q.empty()) {
		u = q.front();
		q.pop();

		for (auto v : graph[u]) {
			if (!visited[v]) {
				visited[v] = 1;
				q.push(v);
			}
		}
	}
}


int main() {
	cin >> n;
	vector<vector<int>> graph(n + 1);

	cin >> m;
	while (m--) {
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}
	
	// 진행
	bfs(1, graph);


	int answer = 0;
	for (int i = 2; i < n + 1; i++) {
		if (visited[i])
			answer++;
	}

	cout << answer;

	return 0;

}