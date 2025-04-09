/*
9:25

어피치에게 합승을 제안하려 한다.

S에서 출발, 각각의 집으로 모두 귀가하는데 소요되는 예상 최저 택시요금이 얼만지 계산하고자 함
양방향 그래프

풀이 : 다익스트라
조건을 어떻게 설정할 것인가 ?!

1. 각 정점에서 A와 B까지 얼마나 걸리는지 최단 비용 체크
2. 출발지에서 모든 정점까지 얼마나 걸리는지 체크
3. 두 값 더해보기
*/

#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#define INF 99999999

using namespace std;

vector<vector<pair<int, int>>> graph(201);
int minDist[2][201][201], visited[201];


void init(int n, vector<vector<int>> &fares){
    for (int i=0;i<fares.size();i++){
        graph[fares[i][0]].push_back({fares[i][1], fares[i][2]});
        graph[fares[i][1]].push_back({fares[i][0], fares[i][2]});
    }
    
    for (int i=1;i<n + 1;i++){
        for (int j=1;j<n + 1;j++){
            minDist[0][i][j] = INF;
            minDist[1][i][j] = INF;
        }
        visited[i] = INF;
    }
}


void dijkstra(int su, int eu, int idx){
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, su});
    minDist[idx][su][su] = 0;
    if (su == eu)
        return;
    
    while (!pq.empty()) {
        int u = pq.top().second;
        int cost = pq.top().first;
        pq.pop();
        
        if (u == eu)
            return;
        
        for (auto v : graph[u]){
            int new_cost = cost + v.second;
            if (minDist[idx][su][v.first] > new_cost){
                minDist[idx][su][v.first] = new_cost;
                pq.push({new_cost, v.first});
            }
        }
    }
}


void dijkstra2(int su){
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, su});
    visited[su] = 0;
    
    while (!pq.empty()) {
        int u = pq.top().second;
        int cost = pq.top().first;
        pq.pop();
        
        for (auto v : graph[u]){
            int new_cost = cost + v.second;
            if (visited[v.first] > new_cost){
                visited[v.first] = new_cost;
                pq.push({new_cost, v.first});
            }
        }
    }
}


int solution(int n, int s, int a, int b, vector<vector<int>> fares) {
    int answer = INF;
    
    init(n, fares);
    
    // 정점 별로 다익스트라 시작
    for (int i=1;i<n + 1;i++){
        dijkstra(i, a, 0);
        dijkstra(i, b, 1);
    }
    // 시작 위치부터 나머지 정점까지 다익스트라 시작
    dijkstra2(s);
    
    // 모든 정점 합 계산
    for (int i=1;i<n + 1;i++){
        // cout << visited[i] << ' ' << minDist[0][i][a] << ' ' << minDist[1][i][b] << '\n';
        answer = min(answer, minDist[0][i][a] + minDist[1][i][b] + visited[i]);
    }
    
    return answer;
}