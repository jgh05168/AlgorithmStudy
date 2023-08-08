T = int(input())

N = 1000001
prime_numbers = [True] * N
prime_numbers[0], prime_numbers[1] = False, False

for i in range(2, int(N ** 0.5) + 1):
    if prime_numbers[i]:
        for j in range(i + i, N, i):
            prime_numbers[j] = False


for tc in range(1, T + 1):
    D, A, B = map(int, input().split())

    cnt = 0
    for idx in range(A, B + 1):
        if A <= idx <= B and prime_numbers[idx] and str(D) in str(idx):
            cnt += 1

    print(f'#{tc} {cnt}')