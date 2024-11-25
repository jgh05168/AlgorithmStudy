'''
개똥벌레

풀이:
누적합으로 ㅆㄱㄴ
동굴을 가로로 세워서 체크해보자
1. 출발지를 1, 종료하는 지점을 -1로 설정한다.
2. w를 탐색하며 누적합을 계산한다.
3. 가장 낮은 값을 갖는 인덱스를 출력한다.
'''

import sys
input = sys.stdin.readline

n, h = map(int, input().split())
check_obstacle = [0] * h

# 종유석과 석순의 출발점, 도착점 관련해서 누적합 해주기
for i in range(n):
    height = int(input())
    # 종유석, 석순 나눠서 생각하기
    if not i % 2:
        check_obstacle[0] += 1
        check_obstacle[height] -= 1
    else:
        check_obstacle[h - height] += 1

# 탐색 : dp에 높이 별로 부숴지는 값 누적해주기
dp = [0] * h
dp[0] = check_obstacle[0]
for i in range(1, h):
    dp[i] = dp[i - 1] + check_obstacle[i]

print(min(dp), dp.count(min(dp)))