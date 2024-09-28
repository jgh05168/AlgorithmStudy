'''
일정금액 지불 -> 10일 회원 자격
회원 대상으로 한 가지 제품 할인
    - 할인 제품은 하루에 하나씩만 구매 가능

자신이 원하는 제품과 수량이 할인하는 날짜와 10일 연속 일치하는 경우에 맞춰서 회원가입
구할 값 : 정현이가 원하는 제품을 모두 할인받을 수 있는 날짝의 총 일수

풀이:
1. 완전탐색 -> 100000 x (10)
'''

from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    want_dict = defaultdict(int)
    n = len(discount)
    
    for i in range(10):
        want_dict[discount[i]] += 1

    for i in range(len(want)):
        if want_dict[want[i]] < number[i]:
            break
    else:
        answer += 1
        
    # 본게임 시작
    for i in range(1, n - 9):
        want_dict[discount[i - 1]] -= 1
        want_dict[discount[i + 9]] += 1

        for i in range(len(want)):
            if want_dict[want[i]] < number[i]:
                break
        else:
            answer += 1
        
    return answer