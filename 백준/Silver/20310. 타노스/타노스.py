
string = list(input())

zeros = 0
ones = 0
for i in range(len(string)):
    if string[i] == '0':
        zeros += 1
    else:
        ones += 1

zeros = zeros // 2
ones = ones // 2

new_string = ''
for _ in range(zeros):
    string = string[::-1]
    string.remove('0')
    string = string[::-1]
for _ in range(ones):
    string.remove('1')
print(''.join(string))