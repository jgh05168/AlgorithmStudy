'''
학교 식당에 먼저 도착한 학생이 나중에 도착한 학생보다 앞쪽에서 대기한다
    -> queue

두 가지 메뉴 제공, 학생들은 두가지 메뉴 중 본인이 좋아하는 메뉴를 결정한 상태

ex)
1 a b: 학생 번호가 양의 정수 a이고 좋아하는 메뉴 번호가 양의 정수 b인 학생 1명이 학교 식당에 도착하여 식당 입구의 맨 뒤에 줄을 서기 시작한다.
2 b: 메뉴 번호가 양의 정수 b인 식사 1인분이 준비되어 식당 입구의 맨 앞에서 대기 중인 학생 1명이 식사를 시작한다

풀이 :
1. 순차대로 입력을 받으며
2. 음식이 없다면 대기, 음식이 있다면 먹고 먹은 list에 저장
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
a, b, c = [], [], []
wait = deque()
for _ in range(n):
    std = list(map(int, input().split()))
    if len(std) == 3:
        wait.append((std[1], std[2]))
    else:
        c_std, food = wait.popleft()
        if std[1] == food:
            a.append(c_std)
        elif std[1] != food:
            b.append(c_std)

while wait:
    c_std, food = wait.popleft()
    c.append(c_std)

if not a:
    print("None")
else:
    print(*sorted(a))
if not b:
    print("None")
else:
    print(*sorted(b))
if not c:
    print("None")
else:
    print(*sorted(c))