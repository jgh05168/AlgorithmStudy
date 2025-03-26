/*
대기실에 거리를 두고 앉도록 안내중임
1. 대기실은 5개며, 각 대기실은 5 x 5
2. 맨해튼거리가 2 이하로 앉지 마라
3. 응시자가 앉은 자리 사이가 파티션으로 막힌 경우에는 허용함

각 대기실별로 거리두기를 지키고 있으면 1을, 한명이라도 지키지 않는다면 0을 배열에 담아 return

풀이 : bfs
각각의 위치에서 bfs 돌아보기
2 이상이면 상관없음. visited 계속 써도 될 듯
'0' 우선탐색 하게 해야함 = 우선순위큐
*/

#include <string>
#include <vector>
#include <cstring>
#include <queue>
#include <iostream>

using namespace std;

int t, n;
int visited[6][6];

int dr[4] = {0, 1, 0, -1};
int dc[4] = {1, 0, -1, 0};

bool isValid(int r, int c){
    return 0 <= r && r < n && 0 <=c && c < n;
}

int bfs(int idx, int sr, int sc, vector<vector<string>> &places){
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> q;
    memset(visited, -1, sizeof(visited));
    q.push({1, {sr, sc}});
    visited[sr][sc] = 0;

    while (!q.empty()){
        int r = q.top().second.first, c = q.top().second.second;
        q.pop();
        
        if (visited[r][c] > 2)
            continue;
        
        for (int d=0;d<4;d++){
            int nr = r + dr[d], nc = c + dc[d];
            if (isValid(nr, nc) && visited[nr][nc] == -1){
                visited[nr][nc] = visited[r][c] + 1;
                // 못앉는 경우가 발생한다면 바로 0 return
                if (visited[nr][nc] <= 2 && places[idx][nr][nc] == 'P' && places[idx][r][c] != 'X')
                    return 0;
                if (places[idx][nr][nc] == 'O')
                    q.push({0, {nr, nc}});
                else if (places[idx][nr][nc] == 'P')
                    q.push({1, {nr, nc}});
                else
                    q.push({2, {nr, nc}});
            }
        }
    }
    return 1;
}


vector<int> solution(vector<vector<string>> places) {
    vector<int> answer;
    t = places.size();
    n = places[0].size();
    
    for (int i=0;i<t;i++){
        int flag = 1;
        for (int r = 0;r <n;r++){
            for (int c=0;c<n;c++){
                if (places[i][r][c] == 'P')
                    flag = bfs(i, r, c, places);
                if (!flag)
                    break;
            }
            if (!flag)
                break;
        }
        answer.push_back(flag);
    }
    
    return answer;
}