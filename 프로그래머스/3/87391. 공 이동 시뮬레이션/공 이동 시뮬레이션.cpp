/*
n x m
0: 열 번호 감소
1: 열 번호 증가
2: 행 번호 감소
3: 행 번호 증가

공은 격자 밖 이동 불가
목적지(쿼리값)가 격자 밖인 경우, 공은 이동하다가 더이상 이동하지 못할 때 멈춤
    - 예시를 잘 보기
가능한 시작점에 공을 두고 쿼리들을 순서대로 실행시키는 경우,
(x, y)에 도착하는 시작점의 개수를 return

쿼리의 개수 : 20만 = O(n) 풀이법을 찾아야함

1. (목표 좌표) - (모든 쿼리 합) 을 한 뒤, row, col이 범위 내에 있는지 확인하기
    - 만약 범위 내(0 ~ n/m)라면 해당 행(열)에서만 가능한 것이다.
    - 범위 밖인 경우에, 전체가 가능한 경우 :
        - 계산값 음수,   쿼리값 >= n, m, 도착지가 반대편 끝인지
        - 계산값 >= n/m, 쿼리값 <= 0, 0, 도착지가 반대편 끝인지
        => 해당 경우 아니면 다 불가능함
-------------------------------------------
2. 도착지부터 역으로 생각해서 범위 늘려나가기
    - 한 쿼리가 들어올 때마다 도착지에서 역으로 계산해 나가기
    - 행의 최대/최소, 열의 최대/최소 값을 비교해서 곱하기
    
.... 나중에 혼자 다시 풀어보자
*/
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long solution(int n, int m, int x, int y, vector<vector<int>> queries) {
    long long x1 = x, y1 = y;
    long long x2 = x, y2 = y;
    
    // 쿼리 역으로 계산해주기
    for(int i = queries.size()-1; i >= 0; i--){
        int order = queries[i][0];
        int dist = queries[i][1];
        
       /*
        * 역추적하기 위해서 밑에 주석을 역추적하는 방향으로 적었음
        * 예를 들어 0번은 원래 왼쪽으로 움직이는 건데, 오른쪽이라고 적었음
        */
        switch(order){
            // 오른쪽
            case 0:
                if(y1 != 0) y1 += dist;
                y2 = min(y2+dist,(long long)m-1);
                if(y1 > m-1) return 0; // 범위 밖으로 나가는지 체크
                break;
            // 왼쪽
            case 1:
                if(y2 != m-1) y2 -= dist;
                y1 = max(y1-dist,0ll);
                if(y2 < 0) return 0;
                break;
            // 아래
            case 2:
                if(x1 != 0) x1 += dist;
                x2 = min(x2+dist,(long long)n-1);
                if(x1 > n-1) return 0;
                break;
            // 위
            case 3:
                if(x2 != n-1) x2 -= dist;
                x1 = max(x1-dist,0ll);
                if(x2 < 0) return 0;
                break;
        }
    }
    return (x2-x1+1)*(y2-y1+1); // 최종 계산
}