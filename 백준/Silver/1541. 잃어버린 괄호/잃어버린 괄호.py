'''
덧셈으로 된 부분먼저 괄호쳐서 계산. 이후 남은 부분 뺄셈으로 순차적으로 계산
'''

def str2int(plus_list):
    lens = len(plus_list)
    changeint = 0
    for val in plus_list:
        changeint += int(val) * (10 ** (lens - 1))
        lens -= 1

    return changeint

equation = input()

# 플러스로 나누어주기
total_list = []
plus_list = []
for i in equation:
    if i != '-':
        plus_list.append(i)
    else:
        total_list.append(plus_list)
        plus_list = []
else:
    total_list.append(plus_list)

# 덧셈을 숫자로 나눠주기
total_calcs = []
plus_calcs = []
plus_list = []
for list in total_list:
    for i in list:
        if i.isdigit():
            plus_list.append(i)
        else:
            plus_calcs.append(plus_list)
            plus_list = []
    else:
        if '+' in list:
            plus_calcs.append(plus_list)
            # 덧셈진행
            add_sum = 0
            for p_list in plus_calcs:
                add_sum += str2int(p_list)
            total_calcs.append(add_sum)
            plus_calcs = []
        else:
            val = str2int(plus_list)
            total_calcs.append(val)
        plus_list = []

if len(total_calcs) == 1:
    print(total_calcs[0])
else:
    minus = total_calcs[0]
    for mval in range(1, len(total_calcs)):
        minus -= total_calcs[mval]
    print(minus)