'''
정해진 총액 이하에서 가능한 한 최대의 총 예산을 배정
1. 모든 요청이 배정될 수 있는 금액에는 그대로 배정
2. 요청이 배정을 넘는 경우 상한액을 정해 그것을 배정

풀이:
이분탐색
총 예산 <= 10**9
nlog10^9 = O(90000)

1. 상한과 하한을 잡고
2. 중간점을 잡고 총액 계산
만약 총액이 안된다면 하한 올리기, 넘친다면 상한 줄이기

'''

import sys
input = sys.stdin.readline


def binary_search(start, end):
    global ans
    mid = (start + end) // 2

    # 종료 조건
    if start >= end:
        return

    tmp = 0
    for i in range(n):
        if cost_list[i] < mid:
            tmp += cost_list[i]
        else:
            tmp += mid

    # 이분탐색
    if tmp <= m:
        ans = max(ans, mid)
        binary_search(mid + 1, end)
    else:
        binary_search(start, mid)



n = int(input())
cost_list = list(map(int, input().split()))
m = int(input())

ans = 0
start, end = 0, max(cost_list) + 1
binary_search(start, end)

print(ans)