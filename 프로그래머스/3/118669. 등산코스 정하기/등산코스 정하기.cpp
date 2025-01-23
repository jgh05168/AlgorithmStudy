/*
n개의 정점, 양방향 그래프
쉼터 혹은 산봉우리를 방문할 때마다 휴식 가능
휴식 없이 이동해야 하는 시간 중 가장 긴 시간 : intensity

출입구 중 한 곳에서 출발하여 산봉우리 중 한 곳만 방문한 뒤 원래의 출입구로 돌아오는 등산코스
출입구는 무조건 한 곳만 방문해야함(중간에 방문 금지)

풀이 : 다익스트라
가는 부분만 체크하면 됨 : 이미 도착지까지 경로는 최소 경로임. 돌아오는데 그거보다 더 커지는 쪽으로 갈 필요 없음

*/

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_map>

#define INF 99999999

using namespace std;


int visited[50001] = {0, };
unordered_map<int, int> summit_dict;

void dijkstra(vector<int> &gates, vector<vector<pair<int, int>>> &graph, vector<int> &answer){
    priority_queue<pair<int, int>> pq;
    for (auto su : gates){
        pq.push({0, su});
        visited[su] = 0;
    }
    
    while (!pq.empty()){
        int w = pq.top().first;
        int u = pq.top().second;
        pq.pop();
        
        if (w > answer[1])
            continue;
        // cout << u << ' '<< w << '\n';
        if (summit_dict[u]){
            if (w < answer[1])
                answer = {u, w};
            else if (w == answer[1])
                answer[0] = min(answer[0], u);
            // cout << answer[0] << " ans " << answer[1] << '\n';
            continue;
        }
        
        for (auto v : graph[u]){
            int new_cost = max(w, v.second);
            if (visited[v.first] > new_cost){
                pq.push({new_cost, v.first});
                visited[v.first] = new_cost;
                // cout << v.first << "   "<< visited[v.first] << '\n';
            }
        }
    }
}

vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
    vector<int> answer;
    answer.push_back(0);
    answer.push_back(INF);
    vector<vector<pair<int, int>>> graph(n + 1);
    
    // 그래프 생성
    for (int i=0;i<paths.size();i++){
        graph[paths[i][0]].push_back({paths[i][1], paths[i][2]});
        graph[paths[i][1]].push_back({paths[i][0], paths[i][2]});
    }
    
    // visited 초기화
    for (int i=0;i<n + 1;i++){
        visited[i] = INF;
    }
    
    // 산봉우리 미리 표시
    for (auto su : summits){
        summit_dict[su] = 1;
    }
    
    dijkstra(gates, graph, answer);
    
    
    return answer;
}