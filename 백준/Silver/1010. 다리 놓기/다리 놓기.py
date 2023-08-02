def factorial(fact):
    if fact == 1 or fact == 0:
        return 1
    else:
        return fact * factorial(fact - 1)

T = int(input())

for tc in range(1, T + 1):

    N, M = list(map(int, input().split()))

    print(int(factorial(M) / (factorial(N) * factorial(M - N))))