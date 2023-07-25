T = int(input())

for test_case in range(1, T + 1):
    sudoku = [list(input().split()) for _ in range(9)]

    c_score = 1
    for row in range(0, len(sudoku)):
        if len(set(sudoku[row])) != 9:
            c_score = 0
        sudoku_column = [row_idx[row] for row_idx in sudoku]
        if len(set(sudoku_column)) != 9:
            c_score = 0
        sudoku_column.clear()
        
    idx_num = 0
    while idx_num < 9:
        three_by_three_arr = []
        for row in range(idx_num, idx_num + 3):
            for col in range(idx_num, idx_num + 3):
                three_by_three_arr.append(sudoku[row][col])
        
        if len(set(three_by_three_arr)) != 9:
            c_score = 0

        three_by_three_arr.clear()
        idx_num += 3

    print(f"#{test_case} {c_score}")

            
            
