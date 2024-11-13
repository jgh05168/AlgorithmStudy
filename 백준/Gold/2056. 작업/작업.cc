#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

// 2056 - 작업
int n, result = 0;
vector<int> inDegree, requireTime, dp;
vector<vector<int>> graph;


void input(){
    cin >> n;
    inDegree.assign(n + 1, 0);
    requireTime.assign(n + 1, 0);
    dp.assign(n + 1, 0);
    graph.assign(n + 1, vector<int> (0, 0));

    for(int cur = 1; cur <= n; cur++){
        int cost, num;
        cin >> cost >> num;
        requireTime[cur] = cost; // 필요한 작업 시간
        inDegree[cur] = num; // 현재 작업의 선행 작업 개수

        for(int i = 0; i < num; i++){
           int pre;
           cin >> pre;
           graph[pre].emplace_back(cur);
        }
    }
}

void topology_sort(){
    queue<int> q;
    for(int i = 1; i <= n; i++){
        if(inDegree[i] == 0){
            q.push(i);
            dp[i] = requireTime[i];
        }
    }

    for(int i = 1; i <= n; i++){
        if(q.empty())   return;

        int cur = q.front();
        result = max(result, dp[cur]);
        q.pop();

        for(int k = 0; k < graph[cur].size(); k++){
            int next = graph[cur][k];
            dp[next] = max(dp[next], dp[cur] + requireTime[next]);
            if(--inDegree[next] == 0){
                q.push(next);
            }
        }
    }
}

int main(){

    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    input();
    topology_sort();
    cout << result;

    return 0;
}