'''
팰린드롬 ?
    - 대칭을 이루는 리스트

- 알아보고자 하는 리스트가 짝수면 펠린드롬이 아니다.

- 홀수인 경우만 탐색

중간부터 잘라서 left, right 이동하며 비교

- 이분탐색

-------------- 실패 ---------------
2차원 dp를 사용해서 풀이

3가지 경우에 대해서 dp 판단
    1. 값이 하나만 존재하는 경우
    2. 값이 자신과 자신과 거리가 1만큼 떨어진 경우
    3. 거리가 2 이상 떨어진 경우

- 이전 dp가 팰린드롬이 아니라면, 나머지 남은 거리 모두 팰린드롬이 아니게 된다.
'''


import sys
input = sys.stdin.readline


N = int(input())
numbers = [0] + list(map(int, input().split()))
M = int(input())
dp = [[0] * (N + 1) for _ in range(N + 1)]

for s in range(1, N + 1):       # 자기 자신만 있는 경우는 무조건 팰린드롬
    dp[s][s] = 1

for s in range(1, N):           # 자기 자신과 자기자신 + 1이 팰린드롬인지 아닌지 확인
    if numbers[s] == numbers[s + 1]:
        dp[s][s + 1] = 1

# count 가 낮은 -> 큰 순서로 판단        -       ex) 값의 차이가 2, 3, 4, ... 순으로 판단한다.
# 이전 단계가 팰린드롬이 아닌 것으로 판별나게 된다면 나머지 결과들도 모두 팰린드롬이 아니게 된다.
for dist in range(2, N + 1):        # : start 와 end 가 몇 칸 떨어져있는지 판단
    for s in range(N - dist + 1):   # 시작 위치
        e = dist + s
        # start(s)와 end(dist + s) 가 같고, 이전 단계 역시 팰린드롬이였다면 업데이트
        if numbers[s] == numbers[e] and dp[s + 1][e - 1] == 1:
            dp[s][e] = 1

for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S][E])
