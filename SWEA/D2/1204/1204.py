T = int(input())

for i in range(0, T):
    num_case = int(input())

    num_list = list(map(int, input().split()))

    num_score = [0 for zero in range(0, 101)]
    
        
    for score in range(0, len(num_list)):
        sc = num_list[score]
        num_score[sc] += 1
    
    max_index = 0
    max = 0
    for index, max_val in enumerate(num_score):
        if (max_val >= max):
            max_index = index
            max = max_val

    print(num_score)
    print("#{num} {max}".format(num = i+1, max = max_index))
    

            
    