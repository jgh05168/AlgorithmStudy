'''
집과 집 사이의 거리 정렬 필요
이분탐색 기준 : 집과 집 사이의 거리 (중요)
'''

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
village = []
for _ in range(N):
    village.append(int(input()))

village.sort()

start, end = 0, village[-1] - village[0]
ans = 0
while start <= end:
    mid = (start + end) // 2

    cnt = 1
    dist = village[0]
    for i in range(len(village)):
        if village[i] - dist >= mid:
            cnt += 1
            dist = village[i]       # 다음 집과 비교에 사용할 현재 집 위치 업데이트

    if cnt >= C:
        ans = max(ans, mid)     # 설치할 수 있는 값들 중 최댓값을 출력
        start = mid + 1
    else:
        end = mid - 1

print(ans)