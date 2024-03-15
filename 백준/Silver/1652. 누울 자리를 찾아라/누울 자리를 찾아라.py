'''
똑바로 연속해서 2칸 이상의 빈 칸이 존재하면 그곳에 누울 수 있다.

범위 밖이거나 빈 칸이 존재할 때 까지 쭉 이어서 눕게된다.
    - 이 점을 만날 때까지 탐색

풀이 :
- for문과 visited 배열이 필요
- 만약 ㄴ누울 수 있는 칸인 경우 flag 생성
- 2칸 이하라면 flag = 0, else: flag = 1
- flag 가 1이라면 += 1
'''

import sys
input = sys.stdin.readline

n = int(input())
room = [list(input().rstrip()) for _ in range(n)]

w_cnt = 0
h_cnt = 0

# 가로로 눕는 경우
for i in range(n):
    j = 0
    while 0 <= j < n:
        if room[i][j] == '.':
            tmp = 0
            while 0 <= j < n and room[i][j] != 'X':
                tmp += 1
                j += 1
            if tmp >= 2:
                w_cnt += 1
        else:
            j += 1

# 세로로 눕는 경우
for j in range(n):
    i = 0
    while 0 <= i < n:
        if room[i][j] == '.':
            tmp = 0
            while 0 <= i < n and room[i][j] != 'X':
                tmp += 1
                i += 1
            if tmp >= 2:
                h_cnt += 1
        else:
            i += 1

print(w_cnt, h_cnt)