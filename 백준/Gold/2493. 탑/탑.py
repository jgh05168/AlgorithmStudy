'''
탑

이전 높이를 저장할 스택 지정
    - 맨 뒤보다 크다면, 그거 출력
    - 맨 뒤보다 현재가 더 크다면, pop 후 큰 게 나올 때까지 진행
        : 어차피 현재가 이전보다 더 크면, 이전 탑의 높이 정보는 필요없게 된다.
'''

import sys
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))

stack = [(0, 0)]
ans = []
for i in range(n):
    cur_h = arr[i]
    flag = 0
    while stack:
        idx, h = stack.pop()
        # 현재 높이와 비교해보기
        if cur_h > h:
            continue
        else:
            ans.append(idx)
            stack.append((idx, h))
            flag = 1
            break
    if not flag:
        ans.append(0)
    stack.append((i + 1, cur_h))

print(*ans)