/*
모임에서 회장을 선출하고자 함
몇 사람만 통하면 모두가 서로 알 수 있다.
- 1점 :  어느 회원이 다른 모든 회원과 친구이면
- 2점 : 다른 모든 회원이 친구이거나, 친구의 친구임을 말한다.
- 3점 : 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친 친 친 임
4, 5점 등은 같은 방법으로 정해진다.

풀이 : 
회원의 수 <= 50, 양방향그래프
회원의 번호는 모든 노드를 탐색하는 데 걸리는 깊이
각 노드 별 bfs 탐색 하면서, 점수를 업데이트하기

*/

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#define INIT cin.tie(0); ios::sync_with_stdio(false);

using namespace std;

int n;
int u, v;
int visited[51] = { 0, };

// 정답을 위한 변수
int min_v = 51;
vector<int> ans;


void bfs(int su, vector<vector<int>> graph) {
	queue<int> q;
	memset(visited, 0, 51 * sizeof(int));
	visited[su] = 1;
	q.push(su);
	int tmp_v = 0;

	while (!q.empty()) {
		u = q.front();
		q.pop();

		for (int i = 0; i < graph[u].size(); i++) {
			v = graph[u][i];
			if (!visited[v]) {
				visited[v] = visited[u] + 1;
				q.push(v);
				tmp_v = max(tmp_v, visited[v] - 1);
				// 가지치기
				if (tmp_v > min_v)
					return;
			}
		}
	}

	// 점수 비교하기
	if (tmp_v < min_v) {
		min_v = tmp_v;
		ans.clear();
		ans.push_back(su);
	}
	else if (tmp_v == min_v) {
		ans.push_back(su);
	}

}


int main() {
	INIT;
	cin >> n;
	vector<vector<int>> graph(n + 1);
	while (1) {
		cin >> u >> v;
		if (u == -1 && v == -1)
			break;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	// 순회하며 bfs 탐색 시작
	for (int p = 1; p < n + 1; p++) {
		bfs(p, graph);
	}

	cout << min_v << ' ' << ans.size() << '\n';
	for (int i = 0; i < ans.size(); i++) cout << ans[i] << ' ';

	return 0;
}