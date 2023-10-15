
string = list(input())

zeros = 0
ones = 0
for i in range(len(string)):
    if string[i] == '0':
        zeros += 1
    else:
        ones += 1

zeros /= 2
ones /= 2

new_string = ''
while zeros:
    new_string += '0'
    zeros -= 1
while ones:
    new_string += '1'
    ones -= 1

print(new_string)