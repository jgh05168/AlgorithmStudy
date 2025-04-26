/*
일정 이상의 알고력과 코딩력이 필요함
- 알고력과 코딩력을 높이기 위해서는 1의 시간이 필요함
- 각 문제를 풀면 올라가는 알고력과 코딩력, 문제 풀이 시간이 정해져있음
- 문제를 하나 푸는 데 문제가 요구하는 시간이 필요하며, 같은 문제를 여러번 풀 수 있다.
주어진 모든 문제들을 풀 수 있는 알고력과 코딩력을 얻는 최단시간을 구하자

풀이 : dp + dfs
모든 문제의 최고차항을 넘으면 현재 depth 리턴
150 x 150
한 번 돌 때, 100번씩 for문 돌아야하나 ..?
*/

#include <string>
#include <vector>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

int MAX_ALP = 0, MAX_COP = 0;
int dp[151][151];

void init(vector<vector<int>> &problems) {
    memset(dp, -1, sizeof(dp));
    for (int i=0;i<problems.size();i++){
        MAX_ALP = max(MAX_ALP, problems[i][0]);
        MAX_COP = max(MAX_COP, problems[i][1]);
    }
}


int topDown(int alp, int cop, vector<vector<int>> &problems) {
    
    if (dp[alp][cop] != -1)
        return dp[alp][cop];
    // 탑다운 알고리즘은 목적지 도착 후 거슬러 올라가는 것임
    if (alp >= MAX_ALP && cop >= MAX_COP)
        return 0;
    
    
    // cout << "### " << depth << ' ' << alp << ' ' << cop << '\n';
    int min_v = 99999999;
    if (alp < MAX_ALP)
        min_v = min(min_v, topDown(alp + 1, cop, problems) + 1);
    if (cop < MAX_COP)
        min_v = min(min_v, topDown(alp, cop + 1, problems) + 1);
    for (int i=0;i<problems.size();i++){
        if (alp >= problems[i][0] && cop >= problems[i][1]){
            int new_alp = min(alp + problems[i][2], MAX_ALP);
            int new_cop = min(cop + problems[i][3], MAX_COP);
            // 업데이트한 값이 변할 때에만 다음 단계로 넘어가야함 : core dumped 방지
            if (new_alp != alp || new_cop != cop)
                min_v = min(min_v, problems[i][4] + topDown(new_alp, new_cop, problems));
        }
    }
    dp[alp][cop] = min_v;
    
    return dp[alp][cop];
}


int solution(int alp, int cop, vector<vector<int>> problems) {
    int answer = 0;
    init(problems);
    
    if (!MAX_ALP && !MAX_COP)
        return answer;
    
    answer = topDown(alp, cop, problems);
    return answer;
}