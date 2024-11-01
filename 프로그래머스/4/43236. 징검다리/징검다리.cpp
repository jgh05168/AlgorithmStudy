/*
바위 중 몇 개를 제거하고자 함

풀이: 이분탐색, 매개변수탐색
1. 바위 정렬
2. 이분탐색 진행
이분탐색 해야할 값 : 돌과 돌 사이의 최소 거리
-> 앞 돌이 제거된 경우, 다음 돌의 거리 계산을 앞 돌의 이전 돌과 해줘야한다.

mid > 두 돌 사이의 거리 : cnt해주기
*/

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int distance, vector<int> rocks, int n) {
    int answer = 0;
    rocks.push_back(0);
    rocks.push_back(distance);
    
    // 정렬
    sort(rocks.begin(), rocks.end());
    
    // 이분탐색 변수 세팅
    int left = 1;
    int right = distance;
    int tmp_dist;
    while (left <= right) {
        int mid = (left + right) / 2;
        // 돌 개수 세어주기
        int cnt = 0;
        int rock_loc = rocks[0];
        int min_dist = distance;
        for (int i=1;i<rocks.size();i++){
            tmp_dist = rocks[i] - rock_loc;
            if (tmp_dist < mid) 
                cnt++;
            else {
                rock_loc = rocks[i];
                min_dist = min(min_dist, tmp_dist);
            }
        }
        // 조건 따져주기
        if (n >= cnt){
            left = mid + 1;
            answer = min_dist;
        }
        else {
            right = mid - 1;
        }
    }
    
    return answer;
}