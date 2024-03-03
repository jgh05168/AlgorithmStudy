'''
왼쪽 한 번 탐색
오른쪽도 탐색

이해관계가 맞다면 count
'''

import sys
input = sys.stdin.readline

h, w = map(int, input().split())
heights = list(map(int, input().split()))
ans = 0
# 하나의 위치를 잡고, 그 두 점 줌 최소 위치에 대해 저장
for i in range(1, w - 1):
    left = max(heights[:i])
    right = max(heights[i + 1:])

    min_height = min(left, right)
    # 좌우의 블럭 높이의 최댓값 중 작은 값이 현재 블록보다 크다면
    # 반대쪽 값도 그 블럭보다 크다. 따라서 작은 값 - 현재블럭 높이 만큼 ans에 저장.
    if heights[i] < min_height:
       ans += min_height - heights[i]

print(ans)