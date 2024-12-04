'''
평범한 베낭

탑다운 방식
'''

def recur(cnt, weight):
    # 범위 넘어가는 경우
    if weight > k or cnt > n:
        return -int(1e9)
    # 마지막에 도착했을 경우, 더 넣을 수 없음
    if cnt == n or weight == k:
        return 0
    if dp[cnt][weight] != -1:
        return dp[cnt][weight]

    dp[cnt][weight] = max(recur(cnt + 1, weight + arr[cnt][0]) + arr[cnt][1], recur(cnt + 1, weight))

    return dp[cnt][weight]


n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 2차원 dp테이블 필요
dp = [[-1] * k for _ in range(n)]

ans = recur(0, 0)

print(ans)