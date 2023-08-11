T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    weight_per_day = list(map(int, input().split()))

    margine = 0
    selling_price = 0       # 주어진 배열 중 가장 비싼 판매가(이 가격에 파는게 가장 good)

    for price in weight_per_day[::-1]:
        # print(price)
        if price >= selling_price:
            selling_price = price
        else:
            margine += selling_price - price

    print(f"#{test_case} {margine}")