/*
젤다는 공주다 !

N x N
상하좌우 인접한 곳으로 한 칸 씩 이동 가능
잃은 금액을 최소로 하여 동굴 건너편까지 가야한다. ( N - 1, N - 1)

링크가 잃을 수밖에 없는 최소 금액은 ?

풀이:
BFS 탐색하면서, 도착할때마다 값 업데이트
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

#define INIT cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
#define INF 10 * 126 * 126

using namespace std;


int n, tmp;
int ans;
vector<vector<int>> graph;
int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };
int visited[126][126] = { 0, };



void dijkstra(int sr, int sc, vector<vector<int>> graph) {
	priority_queue<pair<int, pair<int, int>>> pq;
	visited[sr][sc] = graph[sr][sc];
	pq.push({ -graph[sr][sc], {sr, sc} });

	while (!pq.empty()) {
		int v = -pq.top().first;
		int r = pq.top().second.first;
		int c = pq.top().second.second;
		pq.pop();

		// 도착했으면 값 업데이트
		if (r == n - 1 && c == n - 1) {
			ans = v;
			return;
		}


		for (int d = 0; d < 4; d++) {
			int nr = r + dr[d];
			int nc = c + dc[d];
			if (0 <= nr && nr < n && 0 <= nc && nc < n) {
				int nv = v + graph[nr][nc];
				if (nv < visited[nr][nc]) {
					visited[nr][nc] = nv;
					pq.push({ -nv, {nr, nc} });
				}
			}
		}
	}
}


int main() {
	int t = 0;
	while (1) {
		t++;
		cin >> n;
		vector<vector<int>> graph(n);
		if (!n) break;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> tmp;
				graph[i].push_back(tmp);
				visited[i][j] = INF;
			}
		}


		ans = INF;
		dijkstra(0, 0, graph);

		cout << "Problem " << t << ": " << ans << '\n';


		graph.clear();
	}

	return 0;
}