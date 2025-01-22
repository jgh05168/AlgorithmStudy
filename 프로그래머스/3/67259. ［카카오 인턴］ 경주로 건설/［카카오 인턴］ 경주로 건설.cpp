/*
경주로는 상하좌우 이동 가능
두 빈 칸이 같은 방향으로 이동하면 직선도로 : 100원
직각으로 만나는 경우는 코너 : 500원

풀이 : 배열의 크기가 bfs로도 가능해보인다.
bfs에 들어갈 값 : (행, 열, 현재 이동하는 방향)
배열이 중복되어 방문할수도 있기 때문에 다익스트라를 사용하기

*/


#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

#define INF 999999999

int n;
int visited[4][26][26];
int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

void init(vector<vector<int>> &board) {
    n = board.size();
    for (int d=0;d<4;d++){
        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++)
                visited[d][i][j] = INF;
        }
    }
}

bool isValid(int r, int c){
    return 0 <= r && r < n && 0 <= c && c < n;
}

int dijkstra(int sr, int sc, vector<vector<int>> &board){
    queue<pair<int, pair<int, int>>> pq;
    pq.push({-1, {sr, sc}});
    for (int i=0;i<4;i++)
        visited[i][sr][sc] = 0;
    int ans = INF;
    while (!pq.empty()){
        int cur_d = pq.front().first; // 이전에 왔던 길의 방향을 저장
        int r = pq.front().second.first;
        int c = pq.front().second.second;
        pq.pop();
        
        for (int d = 0;d < 4; d++){
            int nr = r + dr[d], nc = c + dc[d];
            if (isValid(nr, nc) && !board[nr][nc]){
                int new_cost = 100;
                if (cur_d != d)
                    new_cost += 500;
                int total_cost = visited[cur_d][r][c] + new_cost;
                if (visited[d][nr][nc] >= total_cost){
                    // cout << nr << ' ' << nc << ' ' << total_cost << '\n';
                    if (nr == n - 1 && nc == n - 1){
                        ans = min(ans, total_cost - 500);
                        continue;
                    }
                    visited[d][nr][nc] = total_cost;
                    pq.push({d, {nr, nc}});
                }
            }
        }
    }
    
    return ans;
}

int solution(vector<vector<int>> board) {
    init(board);
    
    int answer = dijkstra(0, 0, board);
    for (int i=0;i<n;i++){
        for (int j=0;j<n;j++)
            cout << visited[i][j] << ' ';
        cout << '\n';
    }
    
    return answer;
}