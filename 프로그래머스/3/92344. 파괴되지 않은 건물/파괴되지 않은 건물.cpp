/*
명령 = 25만 -> O(n) or O(nlogn)안에 처리하는 것이 관건이다.
범위 찾아서 반복문 돌리면 250000 * 1000 * 1000 => 시간초과

- 백준 : 개똥벌레 문제처럼 누적합을 진행해주면 된다.
    -> 해당 문제에서는 출발지 = -1, 도착지 + 1 = 1로 설정하여 누적합을 진행했었음
해당 문제는 위 문제의 2차원 풀이를 진행하면 된다.

ex) 3 x 3에서 (0, 0) -> (2, 2) 까지 -2라면
[-2, 0, 0, 2]
[0, 0, 0, 0]
[0, 0, 0, 0]
[2, 0, 0, -2]   해줘야함
# 마지막(3, 3)에 -2 해주는 이유 : 행 x 열 모두 누적합 진행할 때, 두 번 값이 겹치기 때문에 한 번은 빼주어야 함
    -> 이 이유는 2차원 누적합 문제를 풀 때 공통으로 적용되는 사항임
*/

#include <string>
#include <vector>
#include <iostream>

using namespace std;

int n, m;
int prefixSum[1001][1001] = {0, };

int solution(vector<vector<int>> board, vector<vector<int>> skill) {
    int answer = 0;
    n = board.size();
    m = board[0].size();
    
    // 모든 skill에 대해 누적합 진행
    for (int i = 0; i < skill.size();i++){
        // 뺄셈
        if (skill[i][0] == 1) {
            prefixSum[skill[i][1]][skill[i][2]] -= skill[i][5];
            prefixSum[skill[i][1]][skill[i][4] + 1] += skill[i][5];
            prefixSum[skill[i][3] + 1][skill[i][2]] += skill[i][5];
            prefixSum[skill[i][3] + 1][skill[i][4] + 1] -= skill[i][5];
        }  
        // 덧셈
        else {
            prefixSum[skill[i][1]][skill[i][2]] += skill[i][5];
            prefixSum[skill[i][1]][skill[i][4] + 1] -= skill[i][5];
            prefixSum[skill[i][3] + 1][skill[i][2]] -= skill[i][5];
            prefixSum[skill[i][3] + 1][skill[i][4] + 1] += skill[i][5];
        }
    }
    
    
    // 누적합 생성하기 (행 x 열 더해주기)
    // 행
    for (int i=0;i<n;i++){
        for (int j=1;j<m;j++){
            prefixSum[i][j] += prefixSum[i][j - 1];
        }
    }
    // 열
    for (int i=0;i<m;i++){
        for (int j=1;j<n;j++){
            prefixSum[j][i] += prefixSum[j - 1][i];
        }
    }
    
    
    // 원래 배열과 값 더해주며 0보다 큰 값 answer에 더해주기
    for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
            if (board[i][j] + prefixSum[i][j] > 0)
                answer++;
        }
    }
    
    return answer;
}