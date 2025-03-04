/*
각 지역은 유일한 번호로 구분
두 지역 간 길 통과 시간은 1로 동일
최단시간에 부대로 복귀하고자 한다.
적의 방해로 경로가 없어져 복귀가 불가능한 부대원이 있을 수도 있음

풀이 : visited를 -1로 설정한 뒤, destination을 시작으로 해서 각 노드까지 거리를 돌기
*/

#include <string>
#include <vector>
#include <iostream>
#include <cstring>
#include <queue>

using namespace std;

vector<vector<int>> graph(100001);
int visited[100001];

void bfs(int su){
    queue<int> q;
    visited[su] = 0;
    q.push(su);
    
    while (!q.empty()){
        int u = q.front();
        q.pop();
        
        for (auto v: graph[u]){
            if (visited[v] == -1){
                q.push(v);
                visited[v] = visited[u] + 1;
            }
        }
    }
}


vector<int> solution(int n, vector<vector<int>> roads, vector<int> sources, int destination) {
    vector<int> answer;
    memset(visited, -1, sizeof(visited));
    for (int i=0;i<roads.size();i++){
        graph[roads[i][0]].push_back(roads[i][1]);
        graph[roads[i][1]].push_back(roads[i][0]);
    }
    
    bfs(destination);
    
    for (auto loc : sources){
        answer.push_back(visited[loc]);
    }
    
    return answer;
}