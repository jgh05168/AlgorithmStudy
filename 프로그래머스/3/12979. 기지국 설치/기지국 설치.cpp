/*
5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려고 한다.
초기 기지국이 주어지고, 추가로 몇 개를 더 지어야하는지에 대한 최솟값을 구하자

풀이 : 이미 설치된 기지국을 기준으로 나누어서 체크해야함
근데, 겹치는 부분이 있는지는 체크해야함 (그 부분에는 설치 안해도 된다)
- 왼쪽만 겹치게 되어있음 = 마지막 녀석과 비교하기

*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int solution(int n, vector<int> stations, int w) {
    int answer = 0;
    int total_w = 2 * w + 1; // 기지국의 커버 범위

    int current = 1; // 현재 커버되지 않은 아파트 시작
    for (int station : stations) {
        int left = max(1, station - w);  // 기지국이 커버하는 왼쪽 범위
        int right = min(n, station + w); // 기지국이 커버하는 오른쪽 범위

        // 현재 커버되지 않은 구간 길이
        if (current < left) {
            int uncovered = left - current; // 왼쪽부터 현재 커버되지 않는 길이
            answer += (uncovered + total_w - 1) / total_w; // 올림 계산
        }
        current = right + 1; // 다음 커버되지 않은 구간 시작
    }

    // 마지막 남은 구간 처리
    if (current <= n) {
        int uncovered = n - current + 1; // 남은 커버되지 않은 길이
        answer += (uncovered + total_w - 1) / total_w; // 올림 계산
    }

    return answer;
}

