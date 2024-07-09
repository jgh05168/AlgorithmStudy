'''
에라토스테네스의 체
'''

import sys, math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
prime = [True for i in range(1000 + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(1000)) + 1):    # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if prime[i]:     # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= 1000:
            prime[i * j] = False
            j += 1

# 모든 소수 출력
ans = 0
for i in range(n):
    if prime[arr[i]] and arr[i] != 1:
        ans += 1
print(ans)