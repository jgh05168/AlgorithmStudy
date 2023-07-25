N = int(input())

four = N // 1000
N = N - (four * 1000)
three = N // 100
N = N - (three * 100)
two = N // 10
N = N - (two * 10)

sum = four + three + two + N
print(sum)