'''
left, right 반복해가며 최대 위치를 저장하기
이후, 순회하면서 min(left, right)보다 현재 위치가 작으면 값 더해주기
'''

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
arr = list(map(int, input().split()))
left = [0] * w
right = [0] * w

left[0] = arr[0]
right[-1] = arr[-1]
for i in range(1, w):
    left[i] = max(left[i - 1], arr[i])
for i in range(w - 2, -1, -1):
    right[i] = max(right[i + 1], arr[i])

# 순회 시작
ans = 0
for i in range(w):
    height = min(left[i], right[i])
    if arr[i] < height:
        ans += height - arr[i]

print(ans)
