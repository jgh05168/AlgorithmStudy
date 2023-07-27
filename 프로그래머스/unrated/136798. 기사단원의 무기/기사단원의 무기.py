def factor(numb):
    factor_list = []
    number_list = []
    
    for i in range(1, numb + 1):
        number_list.append(i)
    
    for number in number_list:
        cnt = 0
        for i in range(1, int(number ** (1 / 2) + 1)):
            if number % i == 0:
                cnt += 1
                if i < number // i:
                    cnt += 1                
        factor_list.append(cnt)
        
    return factor_list
        

def solution(number, limit, power):
    factor_list = factor(number)
    
    for fact in range(0, len(factor_list)):
        if factor_list[fact] > limit:
            factor_list[fact] = power
    
    return sum(factor_list)