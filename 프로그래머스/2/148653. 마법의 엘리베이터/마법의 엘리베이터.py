'''
0층으로 내려가는 데 필요한 마법의돌 최소 개수

풀이:
최대한 큰 수에서 나눠주는 것이 좋다.
1 - heapq? 시간초과
2 - 그리디? 낮은 자리부터 모듈러연산 하며 5보다 큰 경우면 더해주고, 아니면 뺴주는 식
    3-1. 만약 다음 자릿값이 5 ~ 9에 해당한다면 현재 자릿값을 10 에 도달하는 방향으로 마법의 돌을 사용한다.
    3-2. 만약 다음 자릿값이 0 ~ 4에 해당한다면 현재 자릿값을 0 에 도달하는 방향으로 마법의 돌을 사용한다.
'''

def solution(storey):
    answer = 0
    c = 10
    
    while True:
        v, m = storey // c, storey % c
        if m < 5:
            answer += m
        elif m > 5:
            v += 1
            answer += 10 - m
        else:
            tmp_m = v % c
            if tmp_m >= 5:
                v += 1
                answer += 10 - m
            else:
                answer += m
        if not v:
            break
        else:
            storey = v
        
    return answer