T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = list(map(int, input().split()))

    ans = 0

    for i in range(0, N - 1):
        for j in range(i + 1, N):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    ans = arr[-1] - arr[0]



    print(f'#{test_case} {ans}')