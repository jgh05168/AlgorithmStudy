T = int(input())

for i in range(0, T):
    num_list = list(map(int, input().split()))

    if(len(num_list) != 10):
        exit()
    
    sum = 0
    for j in range(0, len(num_list)):
        if (num_list[j] > 10000):
            exit()

        if(num_list[j] % 2 == 1):
            sum += num_list[j]
        else:
            continue
            

    print("#{num} {sum}".format(num = i+1, sum = sum))
