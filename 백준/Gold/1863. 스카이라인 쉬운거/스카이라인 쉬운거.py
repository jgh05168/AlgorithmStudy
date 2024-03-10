'''
최소 건물이 몇 개인지 확인

풀이 :
- 왼쪽부터 오른쪽으로 탐색할 때 현재보다 큰 값이 들어오면 stack에 push
- 현재 값이 stack의 마지막보다 값이 작다면 건물 += 1
- 값이 같은 경우라면 넘어간다.
- 반복문 다 끝난다면 스택에 남은 값들 다 더해줌

- 실패 -
'''

import sys
input = sys.stdin.readline

n = int(input())
skyline = [0]
buildings = 0
for _ in range(n):
    idx, val = map(int, input().split())
    if skyline[-1] < val:
        skyline.append(val)
    elif skyline[-1] > val:
        c_val = val             # 마지막 값 지정(같은 건물인지 확인용)
        while skyline[-1] > c_val:     # 같은 값이 나올 때까지 빼준다.
            skyline.pop()
            buildings += 1
        if c_val != skyline[-1]:
            skyline.append(val)

while skyline:
    if not skyline[-1]:
        break
    skyline.pop()
    buildings += 1

print(buildings)