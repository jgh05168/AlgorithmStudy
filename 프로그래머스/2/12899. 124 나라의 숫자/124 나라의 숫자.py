'''
1. 124나라에는 자연수만 존재
2. 1, 2, 4로만 모든 수를 표현

풀이:
규칙을 찾아야 함
'''
def solution(n):
    result = []
    while n:
        t = n % 3
        if not t:
            t = 4
            n -= 1
        result.append(str(t))
        n //= 3
    return ''.join(result[::-1])


