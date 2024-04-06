'''
선의 총 길이를 구하는 문제

풀이:
일단 입력 다 받은 다음, 시작점 기준으로 오름차순 정렬해주기.
- 마지막 최장 길이와, 탐색되는 앞자리를 비교해서
- 만약 앞자리가 이전 최장길이보다 길다면 이전 위치는 총 길이에 더해 준 다음
- 시작위치, 끝 위치 업데이트
'''

import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    lines.append(tuple(map(int, input().split())))

lines.sort(key=lambda x: x[0])

start, end = -1000000000, -1000000000
total_length = 0
for cs, ce in lines:
    if cs > end:
        total_length += (end - start)
        start, end = cs, ce
    else:
        end = max(end, ce)

total_length += (end - start)
print(total_length)