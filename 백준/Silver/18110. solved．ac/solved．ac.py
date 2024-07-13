'''
난이도 의견
- 아직 아무 의견이 없다면, 문제의 난이도는 0
- 의견이 하나 이상 있다면, 모든 사람의 난이도 의견의 30% 평균
    - 큰값과 작은값 3명씩을 제외한 평균

그냥 졍렬해서 계산하기
'''

import sys
input = sys.stdin.readline

def my_round(val):
  if val - int(val) >= 0.5:
    return int(val)+1
  else:
    return int(val)

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()
if not n:
    print(0)
else:
    val = my_round(n * 0.15)
    if val > 0:
        average = my_round(sum(arr[val:-val]) / len(arr[val:-val]))
    else:
        average = my_round(sum(arr) / len(arr))
    print(average)