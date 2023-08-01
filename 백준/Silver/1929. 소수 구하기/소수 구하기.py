M, N = list(map(int, input().split()))

check = [True] * (N + 1)
check[0], check[1] = False, False

for number in range(2, N + 1):
    for div in range(number + number, N + 1, number):
        if div % number == 0:
            check[div] = False


for prime in range(M, len(check)):
    if check[prime] == True:
        print(prime)