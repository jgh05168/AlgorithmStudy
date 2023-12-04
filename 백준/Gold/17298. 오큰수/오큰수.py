'''
먼저 정답 배열을 -1로 모두 초기화
스택에는 현재 보고 있는 값이 아닌 이전 값들의 인덱스 번호를 저장한다.

만약 오큰수가 존재할 경우에는 스택을 pop 한 뒤 answer의 배열의 위치에 값 저장
'''

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
stack = []
answer = [-1] * n

stack.append(0)
for i in range(1, n):
    while stack and a[stack[-1]] < a[i]:    # a[stack[-1]] : 오큰수를 비교하기 전 가장 왼쪽의 인덱스 번호의 값
        answer[stack.pop()] = a[i]
    stack.append(i)

print(*answer)