/*
1516 게임 개발

ACM Craft처럼 풀기
- 먼저 조상 노드를 파악한다.
- 이후 한 노드를 만날 때마다 root-- 를 통해 노드 레벨을 낮춰준다.
	- 노드 레벨이 0이 된다면, 현재 노드를 짓는 시간을 저장하고 큐에 삽입
	- 0이 되지 않는다면 레벨만 낮추기
*/
#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define MAX 501
using namespace std;

int n;
vector<int> edge[MAX];//간선 저장(먼저 지어져야 하는 건물)
int inDegree[MAX];//진입 차수 저장
int cost[MAX];//비용 저장
int dp[MAX];//각 건물까지 드는 비용 저장

void topologicalSort() {
	queue<int> q;
	for (int i = 1; i <= n; i++) {
		if (inDegree[i] == 0) {
			q.push(i);
			dp[i] = cost[i];
		}
	}


	while (!q.empty()) {
		int cur_node = q.front();
		q.pop();
		for (int i = 0; i < edge[cur_node].size(); i++) {
			int next = edge[cur_node][i];
			if (--inDegree[next] == 0) {
				q.push(next);

			}
			dp[next] = max(dp[next], cost[next] + dp[cur_node]);
		}

	}
	for (int i = 1; i <= n; i++)
		cout << dp[i] << '\n';
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> cost[i];
		int input;
		cin >> input;
		while (input != -1) {
			inDegree[i]++;
			edge[input].push_back(i);
			cin >> input;
		}

	}
	topologicalSort();
	return 0;
}