/*
n명이 입국심사를 기다림
한 심사대에서는 한 명만 받을 수 있음
모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶다.

풀이 : 이분탐색
이분탐색 변수 : 시간
매개변수탐색 하면서 시간 안에 몇 명씩 상대할 수 있는지 체크하고
n과 비교하기
*/

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#define ll long long

using namespace std;


ll solution(int n, vector<int> times) {
    ll answer = 0;
    int len = times.size();
    
    ll l = 1, r = 100000000000000;
    ll mid;
    while (l < r){
        mid = (l + r) / 2;
        // cout << mid << '#' << l << ' ' << r << '\n';
        ll tmp = 0;
        for (int i=0;i<len;i++){
            tmp += mid / times[i];
        }
        if (tmp < n)
            l = mid + 1;
        else {
            answer = mid;
            r = mid;
        }
    }
    
    return answer;
}