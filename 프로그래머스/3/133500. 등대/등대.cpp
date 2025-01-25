/*
두 노드 중 적어도 하나는 켜져있어야 함
- 현재 도착한 노드에 리프노드가 없으면, 이전 노드를 무조건 켜준다.
- dfs 돌면서 return값이 0이면 현재 light를 킨다. 
- 1번 노드에서만 출발해도 된다.


*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int visited[100001] = {0, };
int turnon[100001] = {0, };

void dfs(int u, vector<vector<int>> &graph){
    visited[u] = 1;
    if (graph[u].empty()){
        turnon[u] = 0;
        // cout << u << '\n';
        return;
    }
        
    for (int i=0;i<graph[u].size();i++){
        if (!visited[graph[u][i]]){
            dfs(graph[u][i], graph);
            if (!turnon[graph[u][i]])
                turnon[u] = 1;
        }
    }
}

int solution(int n, vector<vector<int>> lighthouse) {
    vector<vector<int>> graph(n + 1);
    for (int i=0;i<n - 1;i++){
        graph[lighthouse[i][0]].push_back(lighthouse[i][1]);
        graph[lighthouse[i][1]].push_back(lighthouse[i][0]);
    }
    
    dfs(1, graph);
    
    int answer = 0;
    for (int i=0;i<n + 1;i++){
        if (turnon[i])
            answer++;
    }
    return answer;
}