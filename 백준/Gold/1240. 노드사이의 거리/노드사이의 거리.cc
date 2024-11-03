#include <iostream>
#include <vector>
#include <cstring>
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

const int MAX = 1001;
const int LOG = 10; // 트리의 높이(log)를 결정할 수 있는 최대 값
int depth[MAX];
int parent[MAX][LOG];
int dist[MAX];
vector<pair<int, int>> graph[MAX];

void dfs(int node, int par, int d) {
	depth[node] = depth[par] + 1;
	parent[node][0] = par;
	dist[node] = d;

	for (auto& edge : graph[node]) {
		int next = edge.first;
		int weight = edge.second;
		if (next != par) {
			dfs(next, node, d + weight);
		}
	}
}

void setParent(int n) {
	for (int j = 1; j < LOG; j++) {
		for (int i = 1; i <= n; i++) {
			parent[i][j] = parent[parent[i][j - 1]][j - 1];
		}
	}
}

int lca(int u, int v) {
	if (depth[u] < depth[v]) swap(u, v);

	for (int i = LOG - 1; i >= 0; i--) {
		if (depth[u] - (1 << i) >= depth[v]) {
			u = parent[u][i];
		}
	}

	if (u == v) return u;

	for (int i = LOG - 1; i >= 0; i--) {
		if (parent[u][i] != parent[v][i]) {
			u = parent[u][i];
			v = parent[v][i];
		}
	}

	return parent[u][0];
}

int main() {
	INIT;
	int n, m;
	cin >> n >> m;

	for (int i = 0; i < n - 1; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		graph[u].push_back({ v, w });
		graph[v].push_back({ u, w });
	}

	depth[0] = -1;
	dfs(1, 0, 0); // 루트 노드를 1로 가정
	setParent(n);

	while (m--) {
		int u, v;
		cin >> u >> v;
		int ancestor = lca(u, v);
		cout << dist[u] + dist[v] - 2 * dist[ancestor] << '\n';
	}

	return 0;
}
