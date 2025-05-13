/*
항상 ICN 공항에서 출발함

n <= 10000
알파벳 사전순으로 방문해야함
티켓 idx와 visited idx를 일치시키기
dfs

*/

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<vector<string>> ticket;
vector<string> answer;
int visited[10001];
int flag = 0;

void dfs(string start, int cnt){
    answer.push_back(start);
    
    if (cnt == ticket.size()) 
        flag = 1;
    
    for (int i = 0; i < ticket.size(); i++) {
        if (visited[i]) 
            continue;
        if (ticket[i][0] == start) {
            visited[i] = 1;
            dfs(ticket[i][1], cnt+1);
            
            if (!flag) {
                answer.pop_back();
                visited[i] = 0;
            }
        }
    }
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    ticket = tickets;
    dfs("ICN", 0);
    
    return answer;
}