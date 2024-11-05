/*
ㄹㅇ 다단계
풀이:
1. 회원 이름을 쿼리로 저장한 다음, 그래프 생성
2. seller 돌면서 번 돈 업데이트
*/

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <queue>

using namespace std;

map<string, int> company;

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer(enroll.size());
    // init
    vector<vector<int>> tree(enroll.size());
    for (int i=0;i<enroll.size();i++){
        company.insert({enroll[i], i});
    }
    for (int i=0;i<referral.size();i++){
        if (referral[i] == "-") continue;
        tree[company[enroll[i]]].push_back(company[referral[i]]);
    }
    
    // 판매 시작
    for (int i=0;i<seller.size();i++) {
        int money = amount[i] * 100;
        int u = company[seller[i]];
        queue<pair<int, int>> q;
        q.push({u, money});
        while (!q.empty()){
            u = q.front().first;
            int money = q.front().second;
            q.pop();
            if (!money) break;
            
            // 현재 녀석 머니 업데이트
            answer[u] += money - (money * 10 / 100);
            money = money * 10 / 100;
            for (int v=0;v<tree[u].size();v++){
				q.push({ tree[u][v], money });
            }
        }
        // for (int k=0;k<answer.size();k++){
        //     cout << answer[k] << ' ';
        // }
        // cout << '\n';
    }

    
    return answer;
}