/*
N개의 지점, M개의 도로, W개의 웜홀 존재
- 웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로임
	- 도착하게 된 경우, 시작하였을 때보다 시간이 뒤로 간다 ( 뺄셈해야하나 ?)
한 지점에서 출발하여 시간여행을 시작하여 다시 출발하였던 위치로 돌아왔을 때, 시간이 되돌아가는 경구가 있는지 구하기

풀이 :
음의 가중치가 나올 수도 있다 = 벨만포드
N <= 500, M <= 2500, W <= 200
시간복잡도 : O(VE) = O(N * (M + W))
-------------------------------------------
벨만-포드 알고리즘과 다르게 INF인 경우 continue하면 안되는 이유
https://www.acmicpc.net/board/view/50494
https://www.acmicpc.net/board/view/72995
*/

#include <iostream>
#include <vector>
#include <queue>

#define INF 1e8
#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);

using namespace std;

struct edge {
	int from, to, weight;
};


int tc, N, M, W;
int u, v, w;
int dist[501];
vector<edge> edges;

bool Bellman_Ford() {
	// 출발 지역 0으로 초기화
	// dist[1] = 0;
	for (int u = 0; u < N; u++) {
		// 모든 edge에 대해서 탐색해봐야함
		for (int v = 0; v < edges.size(); v++) {
			edge info = edges[v];
			// // 만약 아직 방문하지 않은 정점이라면, continue
			// if (dist[info.from] == INF) continue;
			
			// 방문했고, 업데이트한 값이 현재 값보다 작다면 업데이트해주기
			if (dist[info.to] > dist[info.from] + info.weight)
				dist[info.to] = dist[info.from] + info.weight;
		}
	}

	// 음수값으로 변한 노드가 있는지 체크하기
	for (int u = 0; u < edges.size(); u++) {
		edge info = edges[u];
		// //방문하지 못한 정점 continue
		// if (dist[info.from] == INF) continue;
		// 음의 사이클 찾아내기 ( 다시 한 번 최소비용이 업데이트된다면 ? 음의 사이클을 갖는 것이다. )
		if (dist[info.to] > dist[info.from] + info.weight)
			return true;
	}
	return false;
}

int main() {
	INIT;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		cin >> N >> M >> W;
		edge tmp;
		for (int i = 0; i < M; i++) {
			cin >> u >> v >> w;
			edges.push_back({ u, v, w });
			edges.push_back({ v, u, w });
		}
		for (int i = 0; i < W; i++) {
			cin >> u >> v >> w;
			edges.push_back({ u, v, -w });
		}

		// 방문거리 초기화
		fill_n(dist, N + 1, INF);

		//벨만-포드 알고리즘 시작
		if (Bellman_Ford()) 
			cout << "YES" << '\n';
		else cout << "NO" << '\n';

		edges.clear();
	}

	return 0;
}