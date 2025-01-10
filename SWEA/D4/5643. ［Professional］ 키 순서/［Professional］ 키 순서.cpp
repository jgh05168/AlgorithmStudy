#include <iostream>
#include <cstring>

using namespace std;

int t, n, m;
int graph[501][501];

int main() {
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        // input()
        memset(graph, 0x3f, sizeof(graph));  // 무한대로 초기화
        cin >> n >> m;
        int a, b;
        for (int i = 0; i < m; i++) {
            cin >> a >> b;
            graph[a][b] = 1;
        }

        // 플로이드-와샬
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    if (graph[i][j] > graph[i][k] + graph[k][j]) {
                        graph[i][j] = graph[i][k] + graph[k][j];
                    }
                }
            }
        }

        // 자신이 몇 번째인지 알 수 있는 학생 수 계산
        int ans = 0;
        for (int i = 1; i <= n; i++) {
            int count = 0;
            for (int j = 1; j <= n; j++) {
                if (graph[i][j] < 0x3f3f3f3f || graph[j][i] < 0x3f3f3f3f) {
                    count++;
                }
            }
            if (count == n - 1) ans++;
        }

        cout << '#' << tc << ' ' << ans << '\n';
    }

    return 0;
}
