colorpaper = int(input())

canvas = [[0] * 100 for _ in range(100)]

for draw in range(colorpaper):
    s_col, s_row = map(int, input().split())

    for row in range(100 - s_row, 100 - (s_row + 10), -1):
        for col in range(s_col - 1, s_col + 10 - 1):
            if 0 <= row < 100 and 0 <= col < 100 and canvas[row][col] == 0:
                canvas[row][col] = 1
            elif 0 <= row < 100 and 0 <= col < 100 and canvas[row][col] == 1:
                continue


cnt = 0
for row in range(100):
    for col in range(100):
        if canvas[row][col] == 1:
            cnt += 1

print(cnt)