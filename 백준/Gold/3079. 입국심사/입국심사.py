'''
k번 심사대에 앉아있는 심사관이 한 명을 심사하는 데 드는 시간은 Tk

풀이:
친구들 <= 10^9 이기 때문에, 이분탐색 써야한다.
-> 시간을 기준으로 풀이하기
-> 최솟값을 찾기 위해
    - start : 0
    - end : 총 친구 수 x 가장 오래 걸리는 시간(최악)

tmp += 시간 // 심사 시간

if tmp < m : (mid + 1, end)
else : (start, mid)
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = [int(input()) for _ in range(n)]

start, end = 0, max(t) * m

while start < end:
    mid = (start + end) // 2
    # tmp 시간 계산해주기
    tmp_time = 0
    for tk in t:
        tmp_time += mid // tk
    if tmp_time < m:
        start = mid + 1
    else:
        end = mid

print(start)