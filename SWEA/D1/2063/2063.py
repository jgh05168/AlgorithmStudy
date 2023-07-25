N = int(input())
if (N % 2 == 0 or N > 199 or N < 9):
    exit()

num_list = list(map(int, input().split()))

for i in range(0, N-1):
    for j in range(i, N):
        if (num_list[i] > num_list[j]):
            num_list[i], num_list[j] = num_list[j], num_list[i]


print(num_list[N//2])