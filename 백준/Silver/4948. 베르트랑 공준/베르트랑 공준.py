check = [True] * (123456 * 2 + 1)
check[0], check[1] = False, False

for number in range(2, int((123456 * 2) ** 0.5) + 1):
    for div in range(number + number, 123456 * 2 + 1, number):
        if check[div] == False:
            continue
        if div % number == 0 and check[div] == True:
            check[div] = False


while 1:
    n = int(input())
    if n < 1 or n > 123456:
        exit()
    m = 2*n

    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, m + 1):
        if check[i] == True:
            cnt += 1

    print(cnt)