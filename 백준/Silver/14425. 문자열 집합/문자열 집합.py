'''
그냥 set에 넣고 숫자 세기
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
str_set = set()
for _ in range(n):
    str_set.add(input().rstrip())

ans = 0
for _ in range(m):
    tmp_str = input().rstrip()
    if tmp_str in str_set:
        ans += 1

print(ans)