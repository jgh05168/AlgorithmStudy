'''
순차적으로 가보면서 매달아본다.
 그 중 최대 중량 출력
'''

import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()
max_weight = 0
for i in range(n):
  max_weight = max(max_weight, (ropes[i] * (n - i)))

print(max_weight)