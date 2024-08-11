'''
빈 칸 개수 세어주기 + 칸 개수만큼 점화식으로 곱해주기
1, 2, 3, 5, 8, 12, ...
'''

import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)

check_bracket = False
tmp_list = []
for i in range(n):
    if s[i] != ' ':
        tmp_list.append(s[i])
        if s[i] == '>':
            print(''.join(tmp_list), end='')
            tmp_list = []
            check_bracket = False
        elif s[i] == '<':
            check_bracket = True
            tmp_list.reverse()
            print(''.join(tmp_list[1:]), end='')
            tmp_list = ['<']
    else:
        if check_bracket:
            tmp_list.append(s[i])
            continue
        tmp_list.reverse()
        print(''.join(tmp_list), end='')
        tmp_list = []
        print(' ', end='')


if tmp_list:
    tmp_list.reverse()
    print(''.join(tmp_list))