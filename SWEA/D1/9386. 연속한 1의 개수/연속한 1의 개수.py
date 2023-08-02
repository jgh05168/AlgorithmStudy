T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    cnt = 0
    cnt_arr = []
    for i in range(0, len(arr)):
        if arr[i] == 1:
            cnt += 1
            cnt_arr.append(cnt)
        else:
            cnt = 0

    max_cnt = 0
    for i in range(0, len(cnt_arr)):
        if cnt_arr[i] > max_cnt:
            max_cnt = cnt_arr[i]

    print(f'#{test_case} {max_cnt}')