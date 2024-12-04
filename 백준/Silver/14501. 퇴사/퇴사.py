'''
탑다운 dp로 작성하기 위한 접근 순서

1. 재귀함수 먼저 생각하기 (지수함수)
2. 갈 수 있는 경우와 없는 경우를 비교하여 max값을 dp테이블에 저장
    - 비교한 값을 현재 dp에 저장하여 return
3. 범위에 대한 예외처리 진행
4. 최종적으로 값 뽑아내기

== dp테이블은 최댓값 or 최솟값을 항상 보장한다.
'''

def recur(idx):
    if idx > n:
        return -int(1e9)        # 어설프게 -1로 설정해두면, 재귀 return되었을 때 최솟값을 보장해주지 못한다.
    if idx == n:
        return 0
    # 이미 dp에 최댓값이 저장되어 있다면
    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(recur(idx + arr[idx][0]) + arr[idx][1], recur(idx + 1))

    # dp[idx]에 값을 저장한 다음 return 시켜주어 새로운 idx로 최대(최소)값을 보내준다.
    return dp[idx]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [-1] * n

recur(0)

print(max(dp))