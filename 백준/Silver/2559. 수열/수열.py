'''
연속적인 며칠 동안의 온도의 합이 가장 큰 지 알아보고자 함

풀이:
완전탐색적으로 풀어나감
for문 사용
'''

# import sys
# input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(k):
    ans += arr[i]

# 시작
tmp = ans
for i in range(k, n):
    tmp += -arr[i - k] + arr[i]
    if ans < tmp:
        ans = tmp

print(ans)