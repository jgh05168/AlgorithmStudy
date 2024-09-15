'''
윷놀이 판은 정해져 있음
1. 처음 시작 칸에 말 4개가 있다.
2. 말은 게임 판에 그려진 화살표의 방향대로만 이동할 수 있다.
    - 말이 파란 칸에서 이동을 시작하면 파란색 화살표를 타야하고
    - 이동하는 도중이거나 파란색이 아닌 칸에서 이동을 시작하면 빨간색 화살표를 타야한다.
    - 말이 도착 칸으로 이동하면 주사위에 나온 수와 관계없이 이동을 마친다.
3. 게임은 10개의 턴으로 이루어진다.
    - 매 턴마다 5면체 주사위를 굴리고, 도착 칸에 있지 않은 말을 하나 골라 주사위의 수만큼 이동
4. 이동을 마치는 칸에 다른 말이 있으면, 그 말을 고를 수 없다.
    - 단, 이동을 마치는 칸이 도착 칸이면 고를 수 있다.
5. 말이 이동을 마칠 때마다 칸에 적혀있는 수가 점수에 추가된다.
점수의 최댓값 구하기

풀이:
dfs : 모든 경우에 대해서 기록해야 한다.
판을 생성해둔 뒤, 점수를 기록
말은 겹치게 두면 안된다.(도착지 제외)
    - 점수를 인덱스로 생각하여 말이 있는지 없는지 확인

'''

from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(depth):
    global ans
    # 종료 조건
    if depth >= len(dice):
        ans = max(sum(yuts), ans)
    else:
        for i in range(len(yuts)):
            # 도착한 윷이라면 넘기기
            if yuts_loc[i] >= 32:
                continue
            # 갈 수 있는 부분 탐색
            move = dice[depth]
            new_loc = yuts_loc[i]
            flag = 0
            for m in range(move):
                # 도착 지점에 다다랐으면
                if new_loc >= 32:
                    flag = 1
                    break
                # 파란 길인 경우
                if not m and len(board[new_loc]) > 1:
                    new_loc = board[new_loc][1]
                else:
                    new_loc = board[new_loc][0]
            # 말이 있는 경우 or 도착지에 다다른 경우는 continue
            if new_loc < 32 and new_loc in yuts_loc.values():
                continue

            yuts_loc[i], bef_loc = new_loc, yuts_loc[i]
            if flag or new_loc == 32:
                dfs(depth + 1)
            else:
                yuts[i] += score[new_loc]
                dfs(depth + 1)
                yuts[i] -= score[new_loc]
            yuts_loc[i] = bef_loc


board = [[1], [2], [3], [4], [5], [6, 20], [7], [8], [9], [10],
         [11, 23], [12], [13], [14], [15], [16, 25], [17], [18], [19], [31],
         [21], [22], [28], [24], [28], [26], [27], [28], [29], [30], [31], [32]]
score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
         13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 40]
dice = list(map(int, input().split()))
yuts = [0, 0, 0, 0]
yuts_loc = defaultdict(int)

ans = 0
dfs(0)
print(ans)
