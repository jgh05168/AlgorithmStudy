/*
1. 외벽과 맞닿아있는 큐
2. 좌표 딕셔너리

*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

void updateOutside(vector<vector<char>>& g, int x, int y) {
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    bool out = false;

    for (int d = 0; d < 4; ++d) {
        int nx = x + dx[d], ny = y + dy[d];
        if (g[nx][ny] == '0') {
            g[x][y] = '0';
            out = true;
            break;
        }
    }

    if (out) {
        for (int d = 0; d < 4; ++d) {
            int nx = x + dx[d], ny = y + dy[d];
            if (g[nx][ny] == '1') {
                g[nx][ny] = '0';
                updateOutside(g, nx, ny);
            }
        }
    }
}

void useFork(vector<vector<char>>& g, char box) {
    int dx[] = {0, 0, 1, -1};
    int dy[] = {1, -1, 0, 0};
    vector<pair<int, int>> pos;

    for (int i = 1; i < g.size() - 1; ++i) {
        for (int j = 1; j < g[0].size() - 1; ++j) {
            if (g[i][j] == box) {
                for (int d = 0; d < 4; ++d) {
                    int ni = i + dx[d], nj = j + dy[d];
                    if (g[ni][nj] == '0') {
                        pos.emplace_back(i, j);
                        break;
                    }
                }
            }
        }
    }

    for (auto& p : pos) {
        g[p.first][p.second] = '0';
        updateOutside(g, p.first, p.second);
    }
}

void useCrane(vector<vector<char>>& g, char box) {
    for (int i = 1; i < g.size() - 1; ++i) {
        for (int j = 1; j < g[0].size() - 1; ++j) {
            if (g[i][j] == box) {
                g[i][j] = '1';
                updateOutside(g, i, j);
            }
        }
    }
}

int solution(vector<string> storage, vector<string> requests) {
    int answer = 0;
    
    int h = storage.size(), w = storage[0].size();
    vector<vector<char>> g(h + 2, vector<char>(w + 2, '0'));

    for (int i = 0; i < h; ++i)
        for (int j = 0; j < w; ++j)
            g[i + 1][j + 1] = storage[i][j];

    for (auto& q : requests) {
        if (q.size() == 1) useFork(g, q[0]);
        else useCrane(g, q[0]);
    }

    int cnt = 0;
    for (int i = 1; i < h + 1; ++i)
        for (int j = 1; j < w + 1; ++j)
            if (g[i][j] != '0' && g[i][j] != '1') ++answer;

    
    return answer;
}