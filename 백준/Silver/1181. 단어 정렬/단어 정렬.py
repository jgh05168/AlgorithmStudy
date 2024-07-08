'''
정렬 알고리즘 사용하기
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = set()
for _ in range(n):
    arr.add(input().rstrip())

ans = sorted(list(arr), key=lambda x: (len(x), x))
for i in range(len(ans)):
    print(ans[i])