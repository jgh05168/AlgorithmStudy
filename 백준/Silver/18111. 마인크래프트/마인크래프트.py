import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
land = [[] * M for _ in range(N)]

max_h = 0
min_h = 500
for i in range(N):
    land[i] = list(map(int, input().split()))

    if max_h < max(land[i]):
        max_h = max(land[i])
    if min_h > min(land[i]):
        min_h = min(land[i])

min_time = 100000000
ans_height = 0
# min 층부터 max 층까지 세보기
for height in range(min_h, max_h + 1):
    remove_block, stack_block = 0, 0
    total = 0
    for row in range(N):
        for col in range(M):
            if land[row][col] < height:
                stack_block += height - land[row][col]
            else:
                remove_block += land[row][col] - height

            # 인벤토리에 블럭이 없는데 칸수를 다 맞추려 했다면 이 층은 불가능
    if stack_block > remove_block + B:
        continue

    # 갖고있는 블럭을 다 사용할 수 있을 때만 정답 계산
    total = stack_block + remove_block * 2
    if min_time >= total:
        min_time = total
        ans_height = height

print(min_time, ans_height)


'''
좋은 설명이 있어서 참고용

# 땅의 높이가 0~256이다.
# 즉, 모든 좌표의 높이가 0~256이므로, 높이의 수를 세는 카운팅 sort가 가능하다.

# H의 최솟값이 항상 0임은 자명하다.
# H의 최댓값은 floor((B + (모든 땅의 높이의 합)) / (N*M))이다
#   내가 가질 수 있는 블럭의 총 수는 B + (모든 땅의 높이의 합)개 일 것이고,
#   그 모든 블럭을 땅을 고르는 데 사용한다면 한 층당 (N*M)개의 블럭이 사용될 것이기 때문이다.
#   층 하나를 모두 채우지 못한 채 남은 블럭은 사용할 수 없으므로 내림(floor)을 해야한다.

import sys
from math import *
pN, pM, pB = map(int, sys.stdin.readline().split())

heightList = [0 for i in range(257)]
for n in range(pN):
    for h in map(int, sys.stdin.readline().split()):
        heightList[h] += 1
        pB += h

maxH = min(floor(pB / (pN*pM)), 256)

# 최적의 답 높이 R은 항상 존재한다. R을 완성하는데에 걸리는 시간을 t라고 하자.
# R + 1층을 완성하는데 걸리는 시간을 t1
# R + 2층을 완성하는데 걸리는 시간을 t2.. 라고 하자
# 항상 t2 >= t1인가? (최적의 층보다 위로 멀어질 수록 완성하는데에 오래 걸리는가?)
# 이를 증명하기 위해 t2 < t1인 경우가 존재한다고 가정하자.
#   R층과 R+1층을 만들 때, 원래의 땅을 R+1층까지 깎고, R층까지 메우는 데에 걸리는 시간이 공통적으로 걸린다.
#   위의 상태를 만든 뒤, R층과 R+1층을 만드는 데에 걸리는 시간을 비교하면 된다.
#   k = M*N 라고 하자.
#   즉, R층과 R+1층 사이의 블럭 a개에 대하여, (0 <= a <= k)
#   2a < k - a여야 한다는 것이다. @1 : 3a < k
#   마찬가지로 R+1층과 R+2층 사이의 블럭 b개에 대하여, (0 <= b <= k)
#   2b > k - b여야 한다는 것이다. @2 : 3b > k
#   이 때, a >= b여야만 한다.
#   그런데 @1과 @2에 대해 3a < k < 3b이므로 a < b가 되어 모순이다.
#   따라서 항상 t2 >= t1이다.
# 이를 귀납적으로 생각하면 최적의 층보다 높은 층을 완성하는 데에 걸리는 시간은 층이 더 높을수록 더 오래 걸린다. (단, B가 충분하지 않다면 걸리는 시간이 무한대로 발산)
# 또한 최적의 층보다 낮은 층을 완성하는 데에 걸리는 시간 역시 층이 더 낮을수록 더 오래 걸린다.

# 이를 증명한 이유는 알고리즘의 정당성 때문이다.
# 어떤 최적의 층을 구하기 위해서 H의 최댓값부터 낮아지며 R을 찾을 것이다.
# 이 때 걸리는 시간이 점점 감소하다가, 만약에 증가하는 시점이 생긴다면 그 직전 층이 무조건 최적의 층임을 증명한 것이기 때문이다.



# 땅고르기 높이 H에 대해, H보다 높은 좌표 X의 땅고르기 시간은 2*(X-H)이다.
#                       H보다 낮은 좌표 Y의 땅고르기 시간은 H-Y이다.

minTime = 2 * pM * pN * 256 + 1
resHeight = 0
for nowH in range(maxH, -1, -1):
    tmpTime = 0
    for i in range(256, nowH, -1):
        tmpTime += 2*(i - nowH)*heightList[i]
    for i in range(nowH):
        tmpTime += (nowH - i)*heightList[i]
    if minTime > tmpTime:
        minTime = tmpTime
    else:
        resHeight = nowH + 1
        break

print(minTime, resHeight)
'''
