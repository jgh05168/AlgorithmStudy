/*
1. 인접한 두 풍선을 고른 뒤, 두 풍선 중 하나를 터트림
2. 풍선들 사이 빈 공간이 있다면, 중앙으로 밀착시킨다.

- 번호가 더 작은 풍선은 한 번만 터트릴 수 있음 -> 나머지는 번호가 더 큰 풍선을 터트려야한다.
최후까지 남기는 것이 가능한 풍선들의 개수를 return

a의 길이 <= 1000000

풀이 : 정렬 불가능

먼저 풍선이 큰 녀석들만 모두 터트린다. 
가운데 풍선을 남기기 위해서는 
1. a < b, b < c
2. a > b, b < c
3. a > b, b > c
--> b가 작은 순간이 있기만 하면 answer가 가능하다.
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int left_a[1000001] = {0, };
int right_a[1000001] = {0, };

int solution(vector<int> a) {
    int answer = 0;
    int n = a.size();
    
    if (a.size() == 1)
        return 1;
    
    left_a[0] = a[0];
    right_a[n - 1] = a[n - 1];
    answer = 2;
    
    // 왼쪽부터 최솟값 찾기
    for (int i=1;i<n;i++){
        left_a[i] = min(left_a[i - 1], a[i]);
    }
    
    // 오른쪽 최솟값 찾기
    for (int i=n - 2;i>=0;i--){
        right_a[i] = min(right_a[i + 1], a[i]);
    }
    
    // 최소가 될 수 있는 경우 구하기
    for (int i=1;i<n - 1;i++){
        if (a[i] < left_a[i - 1] || a[i] < right_a[i + 1])
            answer++;
    }
    
    return answer;
}