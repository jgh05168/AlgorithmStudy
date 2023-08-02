T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    a_b_list = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        a_b_list.append([a, b])

    c_list = []
    P = int(input())
    for i in range(P):
        c = int(input())
        c_list.append(c)

    count_list = []
    for c in c_list:
        count = 0
        for a, b in a_b_list:
            if c >= a and c <= b:
                count += 1
        count_list.append(count)


    print(f"#{tc} {' '.join(str(i) for i in count_list)}")

