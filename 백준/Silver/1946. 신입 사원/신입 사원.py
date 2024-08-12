'''
1. 서류 점수 제일 높은 순으로 sort
2. 이후 면접 순위 for문 사용하여 돌면서,
    - 서류놈의 면접 등수보다 높다면, 등수 update & cnt + 1
'''

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()

    cnt = 1
    max_ = arr[0][1]
    for i in range(1, N):
        if max_ > arr[i][1]:
            cnt += 1
            max_ = arr[i][1]

    print(cnt)