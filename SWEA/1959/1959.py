def mul_and_add(A, B):
    arr = list(zip(A, B))
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i][0] * arr[i][1]
    return sum


T = int(input())
max_index = []

for t in range(1, T+1):
    N, M = map(int, input().split())
    
    A = list(map(int, input().split()))
    if len(A) != N:
        exit()
    B = list(map(int, input().split()))
    if len(B) != M:
        exit()

    max = 0
    if N < M:
        for i in range(0, M - N + 1):
            if len(A) > M:
                break
            # print(len(A), A, M)
            new_max = mul_and_add(A, B)

            if new_max > max:
                max = new_max
            A.insert(0, 0)

    elif M < N:
        for i in range(0, N - M + 1):
            if len(A) > N:
                break

            new_max = mul_and_add(B, A)

            if new_max > max:
                max = new_max
            B.insert(0, 0)
    
    max_index.append(max)



for printmax in range(len(max_index)):
    print(f"#{printmax + 1} {max_index[printmax]}")
    