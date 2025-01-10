#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int t, n, m;
vector<int> to_tall[501];
vector<int> to_small[501];
int cnt[501];

int bfs(const vector<int> graph[], int start) {
    queue<int> q;
    bool visited[501] = {0}; // 방문 체크
    visited[start] = true;
    q.push(start);

    int reach = 0; // 도달 가능한 노드 수
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (int v : graph[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
                reach++;
            }
        }
    }
    return reach; // 자신 제외한 도달 노드 수
}

int main() {
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        // 그래프 초기화
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

        // 각 학생별로 탐색
        for (int i = 1; i <= n; i++) {
            cnt[i] += bfs(to_tall, i); // 자신보다 키가 큰 학생 수
            cnt[i] += bfs(to_small, i); // 자신보다 키가 작은 학생 수
        }

        // 결과 계산
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            if (cnt[i] == n - 1) // 자신 외의 모든 학생과 관계가 있으면
                ans++;
        }

        cout << '#' << tc << ' ' << ans << '\n';
    }

    return 0;
}
