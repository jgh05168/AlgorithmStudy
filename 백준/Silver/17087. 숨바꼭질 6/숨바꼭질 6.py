import sys

input = sys.stdin.readline

# 유클리드 호제법
# a > b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, S = map(int, input().split())

A = list(map(int, input().split()))


min_v = abs(S - A[0])       # 초기 누나좌표 - 동생좌표
for i in range(1, N):
    if min_v > gcd(min_v, abs(S - A[i])):       # 만약 나중 값이 초기 값보다 작을 경우
        min_v = gcd(min_v, abs(S - A[i]))

print(min_v)