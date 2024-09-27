'''
잘린 조각들의 크기와 토핑의  개수에 상관없이 동일한 가짓수의 토핑이 올라가면 공평한 것임

풀이:
가운데 자르고, 슬라이싱 후 set 비교 -> 시간초과
=======
해시맵을 사용
1. 토핑들의 마지막 인덱스를 체크하는 해시맵 생성
2. 첫 토핑 제외한 나머지 토핑들 개수를 오른쪽으로 설정
3. 토핑 리스트 순회
    - 만약 현재 토핑이 오른쪽 토핑에서 더이상 나올 것 같지 않다면, right -= 1
    - 이후 left와 right 개수 비교

'''

from collections import defaultdict

def solution(topping):
    answer = 0
    n = len(topping)

    right = len(set(topping[1:]))
    left = set([topping[0]])
    
    # 1. 토핑들 마지막 인덱스 판단
    topping_dict = defaultdict(int)
    for i in range(len(topping) - 1, 0, -1):
        if not topping_dict[topping[i]]:
            topping_dict[topping[i]] = i
    print(topping_dict)

    # 예외처리
    if n == 1:
        return 0
    if n == 2 and topping[0] == topping[1]:
        return 1
    else:
        for i in range(1, n - 1):
            left.add(topping[i])
            if topping_dict[topping[i]] <= i:
                right -= 1
            if len(left) == right:
                answer += 1
        return answer