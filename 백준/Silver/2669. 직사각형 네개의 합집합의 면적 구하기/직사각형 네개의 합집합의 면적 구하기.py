grid = [[0] * 101 for _ in range(101)]

total = 0
for i in range(4):
    ldx, ldy, rux, ruy = map(int, input().split())
    for row in range(100 - ruy, 100 - ldy):
        for col in range(ldx, rux):
            if grid[row][col] != 1:
                grid[row][col] = 1
                total += 1

print(total)
