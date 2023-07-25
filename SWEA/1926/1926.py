
N = int(input())

if N < 10 or N > 1000:
    exit()

N_list = list(range(1, N + 1))

for case in range(1, N + 1):
    if N >= 100:  # 100 이상의 경우
        if case // 100 == 3 or case // 100 == 6 or case // 100 == 9:
            if case % 100 // 10 == 3 or case % 100 // 10 == 6 or case % 100 // 10 == 9:
                if case % 10 == 3 or case % 10 == 6 or case % 10 == 9:
                    N_list[case - 1] = "---"
                else:
                    N_list[case - 1] = "--"
            elif case % 10 == 3 or case % 10 == 6 or case % 10 == 9:
                N_list[case - 1] = "--"
            else:
                N_list[case - 1] = "-"
        else: 
            if case % 100 // 10 == 3 or case % 100 // 10 == 6 or case % 100 // 10 == 9:
                if case % 10 == 3 or case % 10 == 6 or case % 10 == 9:
                    N_list[case - 1] = "--"
                else:
                    N_list[case - 1] = "-"

            elif case % 10 == 3 or case % 10 == 6 or case % 10 == 9:
                N_list[case - 1] = "-"

    else:  # 100 미만의 경우
        if case // 10 == 3 or case // 10 == 6 or case // 10 == 9:
            if case % 10 == 3 or case % 10 == 6 or case % 10 == 9:
                N_list[case - 1] = "--"
            else:
                N_list[case - 1] = "-"

        elif case % 10 == 3 or case % 10 == 6 or case % 10 == 9:
            N_list[case - 1] = "-"

for i in range(0, len(N_list)):
    print(N_list[i], end=" ")
