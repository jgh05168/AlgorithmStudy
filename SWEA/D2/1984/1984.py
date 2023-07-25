

T = int(input())

for test_case in range(1, T+1):
    case_list = list(map(int, input().split()))

    except_min_max = sorted(case_list)[1:len(case_list)-1]
    sum = 0
    for i in range(0, len(except_min_max)):
        sum += except_min_max[i]
    
    avg = round(sum / len(except_min_max))

    print(f"#{test_case} {int(avg)}")

        