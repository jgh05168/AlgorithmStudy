#include <iostream>
#include <cstring>
#include <queue>
#include <vector>
#include <tuple>

using namespace std;

struct Soldier {
    int move, team, r, c;
};

const int MAX_H = 500;
const int MAX_W = 500;
const int INF = 0x3f3f3f3f;

int grid[MAX_H][MAX_W];
int cnt[MAX_H][MAX_W][2];
int enemy[MAX_H][MAX_W][2];
int dist[MAX_H][MAX_W];

int H, W;

inline bool isValid(int r, int c) {
    return r >= 0 && r < H && c >= 0 && c < W;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N, M, K;
    cin >> N >> H >> W;
    
    vector<vector<int>> b(H, vector<int>(W));
    for (int i = 0; i < H; ++i)
        for (int j = 0; j < W; ++j)
            cin >> b[i][j];
            
    vector<int> r(N);
    for (int i = 0; i < N; ++i)
        cin >> r[i];
    
    // grid: 각 셀의 험준도; -1이면 진입 불가능
    for (int i = 0; i < H; ++i){
        for (int j = 0; j < W; ++j) {
            int terrain = b[i][j];
            grid[i][j] = (terrain > 0 && terrain <= N) ? r[terrain - 1] : -1;
        }
    }
    
    cin >> M;
    vector<Soldier> units(M);
    for (int i = 0; i < M; ++i) {
        cin >> units[i].move >> units[i].team >> units[i].r >> units[i].c;
        cnt[units[i].r][units[i].c][units[i].team] = 1;
        // 인접한 칸 enemy 정보 갱신 (매번 인접칸 4방향 처리)
        int dr[4] = {-1, 1, 0, 0};
        int dc[4] = {0, 0, -1, 1};
        for (int d = 0; d < 4; ++d) {
            int nr = units[i].r + dr[d], nc = units[i].c + dc[d];
            if(isValid(nr, nc)){
                enemy[nr][nc][units[i].team]++;
            }
        }
    }
    
    cin >> K;
    
    // 최대 이동 거리는 각 유닛의 이동력이 최대 20이므로, BFS로 방문할 영역은 작을 수 있음.
    // dist 배열은 매 BFS마다 방문한 좌표만 초기화하여 사용.
    for (int i = 0; i < MAX_H; ++i)
        for (int j = 0; j < MAX_W; ++j)
            dist[i][j] = INF;
    
    int dr[4] = {-1, 1, 0, 0};
    int dc[4] = {0, 0, -1, 1};
    
    while(K--){
        int idx, ey, ex;
        cin >> idx >> ey >> ex;
        idx--; // 0-indexed
        
        // 목표 지점이 진입 불가능하거나 이미 다른 유닛이 있다면 명령 무시
        if(grid[ey][ex] == -1 || (cnt[ey][ex][0] + cnt[ey][ex][1]))
            continue;
        
        int sy = units[idx].r, sx = units[idx].c;
        int t = units[idx].team;
        int maxMove = units[idx].move;
        
        // BFS용 우선순위 큐 (Dijkstra)
        priority_queue< tuple<int,int,int>, vector<tuple<int,int,int>>, greater<tuple<int,int,int>> > pq;
        // 방문한 셀 리스트 (초기화 시킬 부분만 기록)
        vector<pair<int,int>> visited;
        
        // 시작점 초기화
        dist[sy][sx] = 0;
        pq.push({0, sy, sx});
        visited.push_back({sy, sx});
        bool moved = false;
        
        while(!pq.empty()){
            auto [stamina, rPos, cPos] = pq.top();
            pq.pop();
            
            if(dist[rPos][cPos] < stamina)
                continue;
            
            if(rPos == ey && cPos == ex){
                // 출발 유닛의 인접 enemy 정보 감소
                for (int d = 0; d < 4; ++d) {
                    int nr = units[idx].r + dr[d], nc = units[idx].c + dc[d];
                    if(isValid(nr, nc))
                        enemy[nr][nc][t]--;
                }
                // 기존 위치 비우기
                cnt[units[idx].r][units[idx].c][t] = 0;
                // 유닛 이동
                units[idx].r = ey; units[idx].c = ex;
                cnt[ey][ex][t] = 1;
                // 새로운 위치 주변 enemy 정보 증가
                for (int d = 0; d < 4; ++d) {
                    int nr = ey + dr[d], nc = ex + dc[d];
                    if(isValid(nr, nc))
                        enemy[nr][nc][t]++;
                }
                moved = true;
                break;
            }
            
            for (int d = 0; d < 4; ++d) {
                int ny = rPos + dr[d], nx = cPos + dc[d];
                if(!isValid(ny, nx))
                    continue;
                if(grid[ny][nx] == -1)
                    continue;
                int cost = grid[ny][nx];
                if(stamina + cost > maxMove)
                    continue;
                // 상대편 유닛(교전 상태)이 있는 칸은 통과 불가
                if(cnt[ny][nx][1-t])
                    continue;
                // 목표 지점이 아닌 곳에서 상대 진영의 유닛이 인접해 있다면 안됨
                if(!(ny == ey && nx == ex) && enemy[ny][nx][1-t] > 0)
                    continue;
                
                int nCost = stamina + cost;
                if(nCost < dist[ny][nx]){
                    dist[ny][nx] = nCost;
                    pq.push({nCost, ny, nx});
                    visited.push_back({ny, nx});
                }
            }
        }
        
        // 이번 BFS에서 방문했던 셀만 초기화
        for (const auto &p : visited)
            dist[p.first][p.second] = INF;
    }
    
    // 최종 각 유닛의 위치 출력
    for (const auto &unit : units)
        cout << unit.r << " " << unit.c << "\n";
    
    return 0;
}
