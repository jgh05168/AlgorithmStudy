import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

sum_list = [0]
total = 0
for val in arr:
    total += val
    sum_list.append(total)
while M:
    i, j = map(int, input().split())

    print(sum_list[j] - sum_list[i - 1])
    M -= 1