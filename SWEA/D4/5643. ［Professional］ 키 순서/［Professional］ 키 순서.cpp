#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

int t, n, m;
vector<int> to_tall[501];
vector<int> to_small[501];
int visited[501];
int cnt[501];

int dfs(const vector<int> graph[], int u) {
    visited[u] = 1;
    int reach = 1;  // 자신을 포함한 도달 가능한 노드 수
    for (int v : graph[u]) {
        if (!visited[v]) {
            reach += dfs(graph, v);
        }
    }
    return reach;
}

int main() {
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        // input()
        for (int i = 0; i < 501; i++) {
            to_tall[i].clear();
            to_small[i].clear();
        }
        memset(cnt, 0, sizeof(cnt));

        cin >> n >> m;
        int a, b;
        for (int i = 0; i < m; i++) {
            cin >> a >> b;
            to_tall[a].push_back(b);
            to_small[b].push_back(a);
        }

        // start()
        for (int i = 1; i <= n; i++) {
            memset(visited, 0, sizeof(visited));
            int tall_count = dfs(to_tall, i) - 1;  // 자신 제외
            cnt[i] += tall_count;

            memset(visited, 0, sizeof(visited));
            int small_count = dfs(to_small, i) - 1;  // 자신 제외
            cnt[i] += small_count;
        }

        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (cnt[i] == n - 1)  // 자신 외에 모든 학생과 관계가 있으면
                ans++;
        }

        cout << '#' << tc << ' ' << ans << '\n';
    }

    return 0;
}
