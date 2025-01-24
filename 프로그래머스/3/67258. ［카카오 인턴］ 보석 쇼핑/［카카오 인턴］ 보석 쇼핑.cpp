/*
매장 진열대의 특정 범위 물건들을 모두 싹쓸이 구매하는 습관이 있음
진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매

가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아서 return

풀이 : n <= 100000
1. 투포인터
2. dp - 최장 부분 수열 - 2차원 반복문이라 시간초과

여튼 10만 안에 해결해야 하기 때문에 dp 아니면 greedy 사용해야함

투포인터 사용
- m만큼 보석이 없으면 right 중가
- m만큼 있으면 left 증가
*/

#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

int n, m;

vector<int> solution(vector<string> gems) {
    vector<int> answer(2);
    n = gems.size();
    unordered_set<string> s_set;
    
    for (int i=0;i<n;i++){
        if (s_set.empty() || s_set.find(gems[i]) == s_set.end())
            s_set.insert(gems[i]);
    }
    m = s_set.size();
    
    unordered_map<string, int> s_map;
    int left = 0, right = 0;
    int cnt = 0, len = n * 2;
    while (left <= right){
        if (cnt < m){
            if (right >= n)
                break;
            if (!s_map[gems[right]])
                cnt++;
            s_map[gems[right++]]++;
        }
        else {
            // cout << "Imhere"<< ' ' << left << ' ' << right << '\n';
            s_map[gems[left]]--;
            if (!s_map[gems[left]]){
                cnt--;
                if (right - left + 1 < len){
                    len = right - left + 1;
                    answer[0] = left + 1;
                    answer[1] = right;
                }
            }
            left++;
        }
    }
    
    return answer;
}