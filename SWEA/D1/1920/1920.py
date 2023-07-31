T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    add_list = []
 
    for i in range(0, N - M + 1):
        val = 0
        for j in range(0, M):
            val += a[i + j]
        add_list.append(val)
    print(add_list)

    max_val, min_val = add_list[0], add_list[0]
    for j in range(0, len(add_list)):
        if add_list[j] < min_val:
            min_val = add_list[i]
        if add_list[j] > max_val:
            max_val = add_list[i]

    print(max_val, min_val)
    print(f'#{test_case} {max_val - min_val}')

