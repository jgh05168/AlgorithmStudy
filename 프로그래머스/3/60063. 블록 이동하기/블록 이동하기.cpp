/*
10:15

2 x 1 크기의 로봇을 움직여 n x n 위치까지 이동할 수 있도록 프로그래밍 하려고 함
1, 1 위치에서 가로 방향으로 놓여져 있는 상태로 시작함

- 로봇은 회전이 가능하다. 단, 회전하려는 축의 대각선이 막혀있지 않아야함

풀이 : bfs
회전이 가능한지 판단은 두 정점 모두에서 확인해야함
visited는 2개 놓자. 가로, 세로

회전하는 것도 1초 소요
회전축 방향 대각선을 체크할 땐, 다른 한 지점과 거리차이가 1이여야함
뒤 좌표를 체크하는 뭔가 ? -> 그냥 vector써서 sort 때릴까
*/
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

struct DroneState {
    int dir; // 0: 가로, 1: 세로
    pair<int, int> pos1;
    int time;
};

int n;
vector<vector<int>> g_board;
bool visited[2][101][101]; // [방향][row1][col1]

bool isValid(int r, int c) {
    return 0 <= r && r < n && 0 <= c && c < n && g_board[r][c] == 0;
}

pair<int, int> get_pos2(int r1, int c1, int dir) {
    if (dir == 0) { // 가로
        return {r1, c1 + 1};
    } else { // 세로
        return {r1 + 1, c1};
    }
}

int bfs(int sr, int sc) {
    queue<DroneState> q;
    DroneState initialState = {0, {sr, sc}, 0};
    q.push(initialState);
    visited[0][sr][sc] = true;

    int dr[] = {-1, 1, 0, 0};
    int dc[] = {0, 0, -1, 1};

    while (!q.empty()) {
        DroneState current = q.front();
        q.pop();

        int dir = current.dir;
        pair<int, int> p1 = current.pos1;
        int time = current.time;
        pair<int, int> p2 = get_pos2(p1.first, p1.second, dir);

        if ((p1.first == n - 1 && p1.second == n - 1) || (p2.first == n - 1 && p2.second == n - 1)) {
            return time;
        }

        // 1. 상하좌우 이동
        for (int i = 0; i < 4; ++i) {
            pair<int, int> next_p1 = {p1.first + dr[i], p1.second + dc[i]};
            pair<int, int> next_p2 = {p2.first + dr[i], p2.second + dc[i]};

            if (isValid(next_p1.first, next_p1.second) && isValid(next_p2.first, next_p2.second)) {
                if (!visited[dir][next_p1.first][next_p1.second]) {
                    visited[dir][next_p1.first][next_p1.second] = true;
                    q.push({dir, next_p1, time + 1});
                }
            }
        }

        // 2. 회전
        int r1 = p1.first;
        int c1 = p1.second;
        int r2 = p2.first;
        int c2 = p2.second;

        if (dir == 0) { // 가로 -> 세로
            // p1 축 시계
            if (isValid(r1 + 1, c1) && isValid(r2 + 1, c2) && isValid(r1 + 1, c2)) {
                if (!visited[1][r1][c1]) {
                    visited[1][r1][c1] = true;
                    q.push({1, {r1, c1}, time + 1});
                }
            }
            // p1 축 반시계
            if (isValid(r1 - 1, c1) && isValid(r2 - 1, c2) && isValid(r1 - 1, c2)) {
                if (!visited[1][r1 - 1][c1]) {
                    visited[1][r1 - 1][c1] = true;
                    q.push({1, {r1 - 1, c1}, time + 1});
                }
            }
            // p2 축 시계
            if (isValid(r2 + 1, c2) && isValid(r1 + 1, c1) && isValid(r2 + 1, c1)) {
                if (!visited[1][r2][c2]) {
                    visited[1][r2][c2] = true;
                    q.push({1, {r2, c2}, time + 1});
                }
            }
            // p2 축 반시계
            if (isValid(r2 - 1, c2) && isValid(r1 - 1, c1) && isValid(r2 - 1, c1)) {
                if (!visited[1][r2 - 1][c2]) {
                    visited[1][r2 - 1][c2] = true;
                    q.push({1, {r2 - 1, c2}, time + 1});
                }
            }
        } else { // 세로 -> 가로
            // p1 축 시계
            if (isValid(r1, c1 + 1) && isValid(r2, c2 + 1) && isValid(r2, c1 + 1)) {
                if (!visited[0][r1][c1]) {
                    visited[0][r1][c1] = true;
                    q.push({0, {r1, c1}, time + 1});
                }
            }
            // p1 축 반시계
            if (isValid(r1, c1 - 1) && isValid(r2, c2 - 1) && isValid(r2, c1 - 1)) {
                if (!visited[0][r1][c1 - 1]) {
                    visited[0][r1][c1 - 1] = true;
                    q.push({0, {r1, c1 - 1}, time + 1});
                }
            }
            // p2 축 시계
            if (isValid(r2, c2 + 1) && isValid(r1, c1 + 1) && isValid(r1, c2 + 1)) {
                if (!visited[0][r2][c2]) {
                    visited[0][r2][c2] = true;
                    q.push({0, {r2, c2}, time + 1});
                }
            }
            // p2 축 반시계
            if (isValid(r2, c2 - 1) && isValid(r1, c1 - 1) && isValid(r1, c2 - 1)) {
                if (!visited[0][r2][c2 - 1]) {
                    visited[0][r2][c2 - 1] = true;
                    q.push({0, {r2, c2 - 1}, time + 1});
                }
            }
        }
    }
    return -1;
}

int solution(vector<vector<int>> board) {
    g_board = board;
    n = board.size();
    memset(visited, false, sizeof(visited));
    return bfs(0, 0);
}
