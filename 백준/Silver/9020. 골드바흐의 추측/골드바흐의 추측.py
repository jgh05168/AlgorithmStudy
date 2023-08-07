import sys

input = sys.stdin.readline

T = int(input())

# 에라토스테네스의 체(소수 판별)
max_N = 10000
primes = [True] * max_N
primes[0], primes[1] = False, False
for i in range(2, int(max_N ** 0.5) + 1):
    for j in range(i + i, max_N, i):
        if j % i == 0:
            primes[j] = False

for tc in range(1, T + 1):
    N = int(input())


    # 찾고자하는 값 N의 절반부터 값을 낮춰가며 반복문 진행(DP)
    for i in range(N // 2, 1, -1):
        if primes[i] and primes[N - i]:         # 두 수 모두 소수인지 판별
            print(f"{i} {N - i}")               # 만약 두 수 모두 소수라면, 여지없이 출력
            break