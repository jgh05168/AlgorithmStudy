/*
버튼을 누르면 현재 층 + 버튼에 적힌 수 만큼 이동
0보다 작으면 움직이지 않음
0층으로 가기 위한 최소값을 리턴

5보다 작으면 빼는게 이득임
6이상이라면 더하는게 이득임
5라면, 다음 자리수를 확인해봐야함
*/


#include <string>
#include <vector>

using namespace std;

int solution(int storey) {
    int answer = 0;
    
    while (storey){
        int press = storey % 10;
        storey /= 10;
                
        if (!press)
            continue;
        if (press < 5){
            answer += press;
        }
        else if (press > 5){
            answer += 10 - press;
            storey += 1;
        }
        else {
            int tmp_press = storey % 10;
            if (tmp_press + 1 > 5){
                answer += 10 - press;
                storey += 1;
            }
            else {
                answer += press;
            }
        }
    }
    return answer;
}