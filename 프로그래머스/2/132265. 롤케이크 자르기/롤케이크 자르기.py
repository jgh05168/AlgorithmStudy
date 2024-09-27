'''
잘린 조각들의 크기와 토핑의  개수에 상관없이 동일한 가짓수의 토핑이 올라가면 공평한 것임

풀이:
가운데 자르고, 슬라이싱 후 set 비교 -> 시간초과


'''

from collections import defaultdict

def solution(topping):
    answer = 0
    n = len(topping)

    right = len(set(topping))
    left = set()
    
    # 1. 토핑들 마지막 인덱스 판단
    topping_dict = defaultdict(int)
    for i in range(len(topping) - 1, -1, -1):
        if not topping_dict[topping[i]]:
            topping_dict[topping[i]] = i

    # 예외처리
    if n == 1:
        return 0
    if n == 2 and topping[0] == topping[1]:
        return 1
    else:
        for i in range(n):
            left.add(topping[i])
            if topping_dict[topping[i]] <= i:
                right -= 1
            if len(left) == right:
                answer += 1
        return answer