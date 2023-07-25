T = int(input())

for i in range(0, T):
    num_list = list(map(int, input().split()))

    if(len(num_list) != 10):
        exit()

    if (num_list[0] > 10000):
        exit()
    
    max = num_list[0]
    for j in range(1, len(num_list)):
        if (num_list[j] > 10000):
            exit()
        if( num_list[j] > max):
            max = num_list[j]

    print("#{num} {max}".format(num = i+1, max = max))

