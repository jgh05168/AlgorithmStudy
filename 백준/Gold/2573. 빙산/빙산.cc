#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n, m;
int grid[301][301];
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

// 빙산이 있는 위치를 저장하는 큐
queue<pair<int, int>> iceberg;

bool isValid(int r, int c) {
    return (0 <= r && r < n && 0 <= c && c < m);
}

// BFS로 덩어리 개수 확인
int countIcebergParts() {
    int visited[301][301] = {0, };
    int parts = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] > 0 && !visited[i][j]) {
                if (++parts > 1) return 2; // 두 덩어리 이상이면 조기 종료

                queue<pair<int, int>> q;
                q.push({i, j});
                visited[i][j] = 1;

                while (!q.empty()) {
                    auto [r, c] = q.front();
                    q.pop();

                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d], nc = c + dc[d];
                        if (isValid(nr, nc) && grid[nr][nc] > 0 && !visited[nr][nc]) {
                            q.push({nr, nc});
                            visited[nr][nc] = 1;
                        }
                    }
                }
            }
        }
    }
    return parts;
}

// 빙산을 녹이는 함수
void meltIcebergs() {
    int meltMap[301][301] = {0, };
    int size = iceberg.size();

    // 현재 빙산의 위치를 기반으로 녹을 양을 미리 계산
    for (int i = 0; i < size; i++) {
        auto [r, c] = iceberg.front();
        iceberg.pop();

        int melt = 0;
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d], nc = c + dc[d];
            if (isValid(nr, nc) && grid[nr][nc] == 0)
                melt++;
        }

        // 감소량 저장
        meltMap[r][c] = melt;
        iceberg.push({r, c});
    }

    // 실제로 녹이기
    for (int i = 0; i < size; i++) {
        auto [r, c] = iceberg.front();
        iceberg.pop();

        grid[r][c] -= meltMap[r][c];
        if (grid[r][c] > 0) {
            iceberg.push({r, c});
        } else {
            grid[r][c] = 0;
        }
    }
}

// 메인 솔루션 함수
int solution() {
    int years = 0;

    while (!iceberg.empty()) {
        if (countIcebergParts() > 1) return years;

        meltIcebergs();
        years++;

        if (iceberg.empty()) return 0; // 빙산이 전부 녹음
    }
    return 0;
}

// 초기화 함수
void init() {
    cin.tie(0)->sync_with_stdio(false);
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> grid[i][j];
            if (grid[i][j] > 0)
                iceberg.push({i, j});
        }
    }
}

int main() {
    init();
    cout << solution() << '\n';
    return 0;
}
