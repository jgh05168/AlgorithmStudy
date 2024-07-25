'''
퇴사

날짜를 더해가면서, 초과하지 않는 경우, 값 업데이트하기

'''

import sys
input = sys.stdin.readline

n = int(input())
schedule = []
for _ in range(n):
    schedule.append(tuple(map(int, input().split())))

dp = [0] * (n + 1)
for i in range(n):
    # 일정 안에 상담을 진행할 수 있어야 함.
    # 업데이트 범위는 (일정 + 상담에 필요한 날짜) 부터 퇴사날까지 
    for j in range(i + schedule[i][0], n + 1):
        # 이후에는 가치만 놓고 비교하기
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])