/*
택배상자, 1 ~ n번 상자까지 번호 증가하는 순서로 전달됨
한 방향으로만 진행이 가능 : 벨트에 놓인 순서대로 내릴 수 있음
택배 기사님이 알려준 순서에 맞게 실어야함

1. 컨테이너 벨트 맨 앞 상자가 현재 트럭에 실을 순서가 아니라면
    - 상자를 잠시 보조 컨테이너 벨트에 보관함
    - 보조 컨테이너 : 앞뒤로 이동이 가능. 입구 외에는 다른 면이 막혀있음
        - 가장 마지막에 보조 컨테이너 벨트에 보관한 상자부터 꺼내게 된다.
    - 이래도 원하는 순서대로 상자를 못실으면 안실어도 된다.

풀이 :
멈추게 되는 조건을 O(n)으로 찾을 수 있을 것이다.
스택

*/
#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<int> order) {
    int answer = 0;
    stack<int> s;
    
    for (int i=1; i<=order.size(); i++) {
        s.push(i);
        
        while (!s.empty() && s.top() == order[answer]) {
            s.pop();
            answer++;
        }
    }
    
    return answer;
}