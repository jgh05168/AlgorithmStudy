/*
1. 몬스터 공격 우선 저장
2. for 문 돌면서 값 업데이트하기
*/

#include <string>
#include <vector>
#include <iostream>
#include <map>

using namespace std;

map<int, int> attackTime;

int solution(vector<int> bandage, int health, vector<vector<int>> attacks) {
    int answer = 0;
    int lastTime = 0;
    int count = 0;

    for (int i = 0; i < attacks.size(); i++) {
        attackTime[attacks[i][0]] = attacks[i][1];
        if (i == (attacks.size() - 1)) {
            lastTime = attacks[i][0];
        }
    }

    answer = health;

    for (int i = 0; i <= lastTime; i++) {
        if (attackTime[i] != 0) {
            answer -= attackTime[i];
            count = 0;

            // 종료 조건
            if (answer <= 0) {
                answer = -1;
                break;
            }
        } else {
            if (answer <= health && count < bandage[0]) {
                answer += bandage[1];
                count++;

                // 체력 추가 회복
                if (count >= bandage[0]) {
                    answer += bandage[2];
                    count = 0;
                }
            }
        }
        
        // 최대 체력 설정
        if (answer >= health) {
            answer = health;
        }
    }

    return answer;
}