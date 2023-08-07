N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.extend(B)
new_arr = sorted(A)

print(*new_arr)
