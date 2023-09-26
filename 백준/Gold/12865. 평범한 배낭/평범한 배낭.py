'''
가치 합의 최대값을 구하자

냅색 알고리즘(dp)


'''

import sys
input = sys.stdin.readline


# ###### 기본적인 냅색 알고리즘(2차원 배열 사용) : 가방 용량이 작은 쪽 -> 큰 쪽 ######
# n, k = map(int, input().split())  # 물품의 수, 버틸 수 있는 무게
# stuffs = [[0] for _ in range(n)]
# dp = [[0] * (k + 1) for _ in range(n + 1)]
# for i in range(n):
#     w, v = map(int, input().split())
#     stuffs[i] = (w, v)
#
# for stuff in range(1, n + 1):   # 물건 하나씩
#     for weight in range(1, k + 1):  # 1~k무게까지 표 작성
#         w = stuffs[stuff][0]
#         v = stuffs[stuff][1]
#         if j < w:   # 해당 물건이 더 큰 경우, 이전 표값으로 넣기
#             dp[stuff][weight] = dp[stuff - 1][weight]
#         else:   # 해당 물건이 들어가는 사이즈인 경우
#             dp[stuff][weight] = max(dp[stuff - 1][weight], v + dp[stuff - 1][weight - w])    # 이전 값과 비교
#
# print(dp[n][k])


##### 1차원 배열을 사용한 냅색 알고리즘 : 가방 용량이 큰 쪽 -> 작은 쪽 #####
n, k = map(int, input().split())  # 물품의 수, 버틸 수 있는 무게
stuffs = [[0] for _ in range(n + 1)]
dp = [0] * (k + 1)
for i in range(1, n + 1):
    w, v = map(int, input().split())
    stuffs[i] = (w, v)

for stuff in range(1, n + 1):
    for weight in range(k, 0, -1):      # 베낭 용량에 맞춰(줄여가며) 넣을 수 있는 지, 없는 지 확인
        w = stuffs[stuff][0]
        v = stuffs[stuff][1]
        if w <= weight:     # 넣을 수 있는 무게의 범위에서 현재 w보다 클 때까지 넣어보기
           dp[weight] = max(dp[weight], v + dp[weight - w])

print(dp[k])