/*
1-1. 입력된 수가 짝수라면 2로 나눈다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
2. 결과로 나온 수가 1보다 크다면 1번 작업을 반복한다.

나온 꺾은선 그래프를 정적분
- (a, b)가 주어진다면, x=a, x=b, y=0으로 둘러싸인 공간의 면적과 같음
- 0 이상의 수 b 기준 범위 (a, -b)가 주어진다면, x=a, x=n-b, y=0으로 둘러싸인 공간의 면적과 같음
    - n은 k가 초항인 우박수열이 1이 될 때까지의 횟수를 의미함 -> n을 먼저 구하자

주어진 구간의 시작점이 끝점보다 커서 유효하지 않은 구간이 주어질 수 있으며 이때의 정적분 결과는 -1로 정의

범위의 넓이를 구하는 것이 관건임
max정사각형 - 삼각형
*/

#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

vector<int> y_values;
vector<double> integrals;
vector<double> prefixSum;


void getYValue(int k) {
    y_values.push_back(k);
    while (k > 1){
        if (k % 2 == 0){
            k /= 2;
        }
        else{
            k = (k * 3) + 1;
        }
        y_values.push_back(k);
    }
}


void getIntegral(){
    double calc;
    int max_y, min_y;
    for (int i=1;i<y_values.size();i++){
        max_y = max(y_values[i - 1], y_values[i]);
        min_y = max_y - min(y_values[i - 1], y_values[i]);
        calc = max_y - (min_y * 0.5);
        integrals.push_back(calc);
    }
}


void getPrefixSum() {
    prefixSum.push_back(0);
    prefixSum.push_back(integrals[0]);
    for (int i=1;i<integrals.size();i++){
        double val = prefixSum[i] + integrals[i];
        prefixSum.push_back(val);
    }
}


vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> answer;
    
    // 1. 구간별 y값 구하기
    getYValue(k);
    
    // 2. 각 구간별 정적분값 구하기
    getIntegral();
    
    // 3. 정적분 누적합 구하기
    getPrefixSum();

    // 4. 범위에 따라 값 저장하기
    int a, b;
    int n = integrals.size();
    for (auto range : ranges){
        a = range[0];
        if (range[1] <= 0)
            b = n + range[1];
        if (a > b)
            answer.push_back(-1);
        else if (a == b)
            answer.push_back(0);
        else {
            answer.push_back(prefixSum[b] - prefixSum[a]);
        }
    }
    
    return answer;
    

}