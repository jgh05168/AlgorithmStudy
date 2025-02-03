/*
모든 차량이 고속도로에서 단속용 카메라를 한 번은 만나도록 설치하고자 함
차량의 경로가 매개변수로 주어짐
최소 몇 대의 카메라를 설치해야 하는지 return

풀이 : 정렬, 그리디
지점이 끝나는 시점이 빠른 차량 순으로 정렬
지점이 끝나는 시점의 차량이 카메라를 만났는지 확인
-> 만약 안만났으면, 끝에 카메라 설치
새로 들어온 차량의 시작 위치와 마지막 차량의 끝나는 위치를 확인 
끝나는 지점에 카메라 설치 후 지점이 겹치는 차량은 다 빼기
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

bool cmp(vector<int> a, vector<int> b){
    if (a[1] == b[1])
        return a[0] < b[0];
    return a[1] < b[1];
}

int solution(vector<vector<int>> routes) {
    int answer = 0;
    
    // 0. 정렬
    sort(routes.begin(), routes.end(), cmp);
    
    deque<pair<int, int>> q;
    // 1. 순차 탐색
    q.push_back({routes[0][0], routes[0][1]});
    int camera = 0;
    for (int i=1;i<routes.size();i++){
        int start = routes[i][0], end = routes[i][1];
        if (!q.empty() && start > q.front().second){
            camera = q.front().second;
            while (!q.empty() && q.front().first <= camera && camera <= q.front().second)
                q.pop_front();
            answer++;
        }
        q.push_back({start, end});
    }
    if (!q.empty())
        answer++;
    
    return answer;
}