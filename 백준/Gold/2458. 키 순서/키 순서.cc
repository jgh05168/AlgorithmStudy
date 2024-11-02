/*
두 학생의 키를 비교한 결과의 일부가 주어짐.
N명의 학생들의 키는 모두 다르다.

풀이:
그래프를 순회하며 레벨을 따져보기
자신이 몇 번째 노드이고, 자신에서 몇 군데를 더 갈 수 있는지에 대해서 체크
- 한 노드에서 정방향으로 한 번, 역방향으로 한 번 가 본 뒤, 두 군데의 합이 N - 1이라면 다 찾을 수 있는 경우이다.
*/

#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n, m;
int s, e;
int visited[501] = { 0, };
int cnt[501] = { 0, };

void bfs(vector<vector<int>> graph, int su) {
	queue<int> q;
	q.push(su);
	visited[su] = 1;

	while (!q.empty()) {
		int u = q.front();
		q.pop();

		for (int i = 0; i < graph[u].size(); i++) {
			int v = graph[u][i];
			if (!visited[v]) {
				q.push(v);
				visited[v] = 1;
				cnt[v]++;
			}
		}
	}
}


int main() {
	cin >> n >> m;
	vector<vector<int>> graph(n + 1);
	vector<vector<int>> rev_graph(n + 1);

	while (m--) {
		cin >> s >> e;
		graph[s].push_back(e);
		rev_graph[e].push_back(s);
	}

	for (int i = 1; i < n + 1; i++) {
		memset(visited, 0, 501 * sizeof(int));
		bfs(graph, i);
		memset(visited, 0, 501 * sizeof(int));
		bfs(rev_graph, i);
	}

	int ans = 0;
	for (int i = 1; i < n + 1; i++) {
		if (cnt[i] == n - 1)
			ans++;
	}

	cout << ans << '\n';


	return 0;
}