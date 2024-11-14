/*
멘토와 1대1
n명의 멘토, 1 ~ k번으로 분류되는 상담유형
각 멘토는 k개 상담유형 중 하나만 담당 가능
멘토는 자신이 담당하는 유형의 상담만 가능
상담 시간은 정확히 참가자가 요청한 시간만큼 걸림

- 상담 규칙
1. 참가자의 상담 유형을 담당하는 멘토 중 삼당 중이 아닌 멘토와 상담 시작
2. 모두 상담중이라면 차례를 기다림
	- 기다린 시간은 참가자가 요청했을 때부터 상담을 시작할 때까지
3. 먼저 상담 요청한 참가자 우선대로 상담 진행

참가자의 상담 요청 정보가 주어질 때, 기다린 시간의 합이 최소가 되도록 멘토 인원을 정하고자 함
각 유형별로 멘토 인원이 적어도 한 명 이상

문제 범위 :
n <= 20
상담요청 <= 300

문제 풀이 방법 :
1. reps를 먼저 분석하여 각 유형에 몇 명의 사람이 있는지 체크
2. 모든 멘토를 한 명 씩 넣어두고 시작
3. 한 명 씩 맡아서 상담 진행해보고, 대기시간 긴 곳 찾아서 추가로 사람 넣기
	-> 이거 반복
*/

#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>

using namespace std;

vector<vector<int>> orders; // 분배가능한 모든 경우의 수

// 모든 경우의 수를 구하는 함수(남은 인원, 유형, 컨테이너)
void backtracking(int remain, int idx, vector<int> order){
    // 모든 인원을 담았으면 orders에 추가
    if(remain <= 0){
        orders.push_back(order);
        return;
    }
    
    for(int i = idx; i < order.size(); i++){
        order[i]++;
        backtracking(remain-1,i,order);
        order[i]--;
    }
}

// 각 경우의 수에 맞춰 시뮬레이션을 돌림(순서,요청들)
int simulation(vector<int> order, vector<vector<int>> reqs){
    // 오름차순으로 뽑히는 우선순위큐를 유형의 수만큼 만듦
    priority_queue<int,vector<int>,greater<int>> pq[order.size()];
    int result = 0; // 대기 시간의 합
    
    
    for(int i = 1; i < order.size(); i++){
        // 각 경우의 수에 맞춰 각 우선순위큐에 담음
        for(int j = 0; j < order[i]; j++) pq[i].push(0);
    }
    
    for(auto req : reqs){
        int arrive = req[0]; // 요청 시각
        int time = req[1]; // 상담 시각
        int idx = req[2]; // 상담 유형
        
        // 해당 유형의 우선순위 큐에서 하나 뽑는다.
        int picked = pq[idx].top();
        pq[idx].pop();
        
        // 멘토의 시간 > 요청 시각
        if(picked > arrive){
            result += picked-arrive;
            pq[idx].push(picked+time);
        }
        
        // 멘토의 시간 < 요청 시각
        else if(picked < arrive) pq[idx].push(arrive+time);
        
        // 멘토의 시간 == 요청 시각
        else pq[idx].push(picked+time);
    }
    
    return result;
}

int solution(int k, int n, vector<vector<int>> reqs) {
    int answer = 99999999;
    
    vector<int> kind(k+1,1);
    backtracking(n-k,1,kind);
    
    for(auto order : orders){
        answer = min(answer,simulation(order,reqs));
    }
    return answer;
}