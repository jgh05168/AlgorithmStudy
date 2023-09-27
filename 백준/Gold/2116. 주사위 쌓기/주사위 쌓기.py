'''
주사위쌓기

쌓을 때 윗면의 숫자와 아랫면의 숫자는 같아야 한다.
    - 1번 주사위는 마음대로 놓을 수 있다.

1번 주사위는 6번의 경우에 대해 모두 생각
쌓아지는 주사위 번호를 dictionary를 사용하여 짝을 지어준다.

남는 숫자들 중 최대값을 더해주면서 올라간다.

알고리즘 : 백트래킹
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

dict = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}


def recur(dice, val, top_idx, top):
    global max_v
    if dice == N:
        if max_v < val:
            max_v = val
        return

    # 다음 top 값 찾기
    for idx in range(6):
        if dices[dice][idx] == top:
            ntop = dices[dice][dict[idx]]
            ntop_idx = idx
            break

    temp = 0
    for num in range(6):
        if dices[dice][num] == top or dices[dice][num] == ntop:
            continue
        else:
            if temp < dices[dice][num]:
                temp = dices[dice][num]

    recur(dice + 1, val + temp, ntop_idx, ntop)

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
max_v = 0

for first in range(6):
    recur(0, 0, first, dices[0][first])

print(max_v)