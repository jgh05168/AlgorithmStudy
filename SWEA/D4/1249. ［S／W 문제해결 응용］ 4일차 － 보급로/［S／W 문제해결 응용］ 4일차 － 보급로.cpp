#include <iostream>
#include <queue>
#include <string>

using namespace std;

int t, n;
int grid[101][101];
int visited[101][101];

int dr[4] = { 0, 1, 0, -1 };
int dc[4] = { 1, 0, -1, 0 };

void init() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s; cin >> s;
        for (int j = 0; j < s.size(); j++)
            grid[i][j] = (int)s[j] - '0';
    }
    fill(&visited[0][0], &visited[100][101], 10001); // visited 초기화
}

int bfs(int sr, int sc) {
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<>> pq;
    pq.push({ 0, {sr, sc} });
    visited[sr][sc] = 0;

    while (!pq.empty()) {
        int cost = pq.top().first;
        int r = pq.top().second.first, c = pq.top().second.second;
        pq.pop();

        if (r == n - 1 && c == n - 1) // 목적지 도달 시 종료
            return cost;

        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (0 <= nr && nr < n && 0 <= nc && nc < n && visited[nr][nc] > cost + grid[nr][nc]) {
                visited[nr][nc] = cost + grid[nr][nc];
                pq.push({ visited[nr][nc], {nr, nc} });
            }
        }
    }
    return -1;
}

int main() {
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        init();
        int ans = bfs(0, 0);
        cout << '#' << tc << ' ' << ans << '\n';
    }
    return 0;
}
