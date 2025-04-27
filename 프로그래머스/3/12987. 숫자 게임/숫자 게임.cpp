/*
A, B 모두 정렬하기
투포인터로 문제 해결
*/

#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    int answer = 0;
    
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    
    int last_a, last_b;
    while (!A.empty()){
        last_a = A.back();
        last_b = B.back();
        A.pop_back();
        
        if (last_a < last_b){
            answer++;
            B.pop_back();
        }
    }
    return answer;
}