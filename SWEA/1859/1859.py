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


# https://herbi1411.tistory.com/entry/SWEA-%EB%B0%B1%EB%A7%8C-%EC%9E%A5%EC%9E%90-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B81859-PYTHON 참고함