'''
dp를 무한대로 설정해두면 ?

해보자
'''

import sys
input = sys.stdin.readline

def recur(a, b, idx, move_cnt):
    global min_move
    if min_move <= move_cnt:
        return
    if idx == m:
        min_move = min(min_move, move_cnt)
        return
    else:
        recur(a, open_door[idx], idx + 1, move_cnt + abs(open_door[idx] - b))
        recur(open_door[idx], b, idx + 1, move_cnt + abs(open_door[idx] - a))

n = int(input())
a, b = map(int, input().split())
a -= 1
b -= 1
open_door = []
m = int(input())
for _ in range(m):
    x = int(input())
    open_door.append(x - 1)

min_move = int(1e9)

recur(a, b, 0, 0)

print(min_move)