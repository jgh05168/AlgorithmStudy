'''
x일동안 가장 많이 들어온 방문자 수와 그 기간

풀이:
1차원 리스트 순회하며 기간 세어주기
- 더 큰 구간이 있다면 업데이트
- 같은 구간이 있다면 구간 수 세어주기
'''

import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

visitor = 0
cnt = 1
for i in range(x):
    visitor += arr[i]

ans = visitor
for i in range(x, n):
    visitor += arr[i]
    visitor -= arr[i - x]
    if visitor > ans:
        ans = visitor
        cnt = 1
    elif visitor == ans:
        cnt += 1

if not visitor:
    print("SAD")
else:
    print(ans)
    print(cnt)