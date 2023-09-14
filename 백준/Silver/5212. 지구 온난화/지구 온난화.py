'''
일단 한번 탐색해서 섬을 없애준다.

이후 row, col을 개별 탐색하면서 지도의 크기를 줄여준다.

'''

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

sea_list = []
# 50년 후 섬들부터 없애주자
for row in range(R):
    for col in range(C):
        if grid[row][col] == 'X':
            sea = 0
            for d in range(len(dr)):
                nrow, ncol = row + dr[d], col + dc[d]
                if 0 > nrow or nrow >= R or 0 > ncol or ncol >= C or grid[nrow][ncol] == '.':
                    sea += 1
            if sea > 2:
                sea_list.append((row, col))

for row, col in sea_list:
    grid[row][col] = '.'

land_list = []
for row in range(R):
    for col in range(C):
        if grid[row][col] == 'X':
            land_list.append((row, col))

land_list.sort(key=lambda x: x[0])
min_row, max_row = land_list[0][0], land_list[-1][0]

land_list.sort(key=lambda x: x[1])
min_col, max_col = land_list[0][1], land_list[-1][1]

for i in range(min_row, max_row + 1):
    for j in range(min_col, max_col + 1):
        print(grid[i][j], end='')
    print()