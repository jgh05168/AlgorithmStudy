arr = [list(map(int, input().split())) for _ in range(9)]

max_r, max_c, max_v = 0, 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_v:
            max_r = i
            max_c = j
            max_v = arr[i][j]

print(max_v)
print(max_r + 1, max_c + 1)