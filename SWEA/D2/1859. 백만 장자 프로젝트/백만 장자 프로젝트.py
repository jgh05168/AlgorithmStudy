T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    weight_per_day = list(map(int, input().split()))

    margine = 0
    selling_price = 0

    for price in weight_per_day[::-1]:
        if price >= selling_price:
            selling_price = price
        else:
            margine += selling_price - price

    print(f"#{test_case} {margine}")