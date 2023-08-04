n = int(input())        # alpha count

poster = list(input())  # 후위표현식 입력
alphabets = sorted(set(list(filter(str.isalpha, poster))))      # 후위표현식 내부 알파벳 list

numbers = []

for i in range(n):
    numbers.append(input())         # 각 alphabet 값들 입력


alphabet_list = dict(zip(alphabets, numbers))
# print(alphabet_list)
for idx in range(len(poster)):
    if poster[idx].isalpha and poster[idx] in alphabet_list.keys():
        poster[idx] = str(alphabet_list[poster[idx]])
# print(poster)
stack = []
for calc in poster:
    if calc.isdigit():
        stack.append(calc)
    else:
        if len(stack) == 1:
            break
        x, y = float(stack.pop(-2)), float(stack.pop(-1))
        if calc == '*':
            stack.append(str(x * y))
        elif calc == '/':
            stack.append(str(x / y))
        elif calc == '+':
            stack.append(str(x + y))
        elif calc == '-':
            stack.append(str(x - y))


print(f"{float(stack[0]):.2f}")