/*
ACM Craft

-  이전 두 건물을 모두 지어야 함

풀이:
- bfs로 진행 
-  출발은 전체가 다 해봐야 한다.(도착지에 모두  도착 후, 출발지 노드가 지어졌는지 확인해보기
- 이전 건물 확인을 위한 역방향 그래프도 만들어주기
- 만약 dp 값보다 작은 값이 완성된다면, bfs 큐에 저장 x
--------------- 시간초과 ------------------
모든 노드들에 대한 경우의 수를 다 살펴보는 경우는 불가능하다.
1. degree 정보를 통해 조상 노드를 추려낸 뒤, 이놈들에 대해서 게임을 진행하자.
2. 초기 조상 노드들을 모두 queue에 삽입시킨 후 최댓값으로 업데이트 시키는 방식으로 가자(순차적, 바텀업 방식처럼)
*/

#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>

using namespace std;

int t, n, k;
int value[1001];
int dp[1001];


int main() {
	cin.tie(NULL); ios::sync_with_stdio(false);

	cin >> t;
	for (int tc = 0; tc < t; tc++) {
		cin >> n >> k;
		for (int i = 1; i < n + 1; i++) cin >> value[i];
		vector<vector<int>> graph(n + 1);
		vector<int> degree(n + 1);
		int x, y;
		for (int i = 0; i < k; i++) {
			cin >> x >> y;
			graph[x].push_back(y);
			degree[y]++;		// 내 위에 몇 개의 노드가 있는지 체크해주기
		}
		int dest;
		cin >> dest;

		memset(dp, 0, sizeof(dp));
		// 초기 조상노드들을 전부 다 넣어준다.
		queue<int> q;
		for (int i = 1; i < n + 1; i++) {
			if (!degree[i]) {
				q.push(i);
				dp[i] = value[i];
			}
		}
		// 전체 가능한 경우에서 노드 탐색 시작
		while (!q.empty()) {
			int u = q.front();
			q.pop();


			for (int v : graph[u]) {
				int new_value = value[v];
				dp[v] = max(dp[v], dp[u] + new_value);
				degree[v]--;		// 내 위에 있는 노드 개수를 하나 내려줌
				// 만약 v가 조상 노드가 된다면, queue에 push
				if (!degree[v]) q.push(v);
			}
		}

		cout << dp[dest] << '\n';
	}


	return  0;
}