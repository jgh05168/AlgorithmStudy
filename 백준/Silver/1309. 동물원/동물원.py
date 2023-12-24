import sys
input = sys.stdin.readline

n = int(input())

b2 = 1
b1 = 3
cur_v = 0
for i in range(2, n + 1):
   cur_v = 2 * b1 + b2  # 새로 추가된 우리에 넣는 경우와 넣지 않는 경우를 각각 생각
   b2 = b1
   b1 = cur_v

if n == 1:
    print(b1)
else:
    print(cur_v % 9901)