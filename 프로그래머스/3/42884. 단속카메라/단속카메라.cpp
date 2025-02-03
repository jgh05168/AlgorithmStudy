#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(vector<int> a, vector<int> b) {
    return a[1] < b[1];  // 종료 지점을 기준으로 정렬
}

int solution(vector<vector<int>> routes) {
    int answer = 0;
    
    // 종료 지점 기준으로 정렬
    sort(routes.begin(), routes.end(), cmp);
    
    int camera = -30001;  // 카메라 설치 위치 (초기값: 고속도로 범위 밖)
    
    for (const auto& route : routes) {
        int start = route[0], end = route[1];
        
        // 현재 차량이 기존 카메라로 단속되지 않는 경우, 새로운 카메라 설치
        if (start > camera) {
            camera = end;  // 현재 차량의 종료 지점에 카메라 설치
            answer++;
        }
    }
    
    return answer;
}
