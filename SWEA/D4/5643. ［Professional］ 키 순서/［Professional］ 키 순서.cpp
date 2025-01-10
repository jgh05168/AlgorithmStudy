#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int t, n, m;
vector<vector<int>> graph(501);
vector<vector<int>> rev_graph(501);
int visited[501];
int total_tall[501];   // 자신보다 키가 큰 학생 수
int total_small[501];  // 자신보다 키가 작은 학생 수

void init() {
    for (int i = 0; i <= n; i++) {
        graph[i].clear();
        rev_graph[i].clear();
    }
    memset(total_tall, 0, sizeof(total_tall));
    memset(total_small, 0, sizeof(total_small));

    cin >> n >> m;

    int a, b;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        graph[a].push_back(b);     // 정방향 그래프
        rev_graph[b].push_back(a); // 역방향 그래프
    }
}

int bfs(int start, const vector<vector<int>> &graph) {
    memset(visited, 0, sizeof(visited));
    queue<int> q;
    q.push(start);
    visited[start] = 1;

    int count = 0; // 도달 가능한 노드 수
    while (!q.empty()) {
        int u = q.front();
        q.pop();

        for (int v : graph[u]) {
            if (!visited[v]) {
                visited[v] = 1;
                q.push(v);
                count++;
            }
        }
    }
    return count;
}

int main() {
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        init();

        for (int i = 1; i <= n; i++) {
            // BFS로 자신보다 키가 큰 학생 수 탐색
            total_tall[i] = bfs(i, graph);
            // BFS로 자신보다 키가 작은 학생 수 탐색
            total_small[i] = bfs(i, rev_graph);
        }

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            // 자신보다 키가 큰 학생 수 + 자신보다 키가 작은 학생 수 == n - 1
            if (total_tall[i] + total_small[i] == n - 1) {
                ans++;
            }
        }

        cout << '#' << tc << ' ' << ans << '\n';
    }

    return 0;
}
