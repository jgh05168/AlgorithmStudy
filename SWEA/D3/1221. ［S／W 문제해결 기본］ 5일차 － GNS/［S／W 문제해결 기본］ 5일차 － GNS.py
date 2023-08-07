def change2Int(string_list, int_list):
    for numb in string_list:
        if numb == 'ZRO':
            int_list.append(0)
        elif numb == 'ONE':
            int_list.append(1)
        elif numb == 'TWO':
            int_list.append(2)
        elif numb == 'THR':
            int_list.append(3)
        elif numb == 'FOR':
            int_list.append(4)
        elif numb == 'FIV':
            int_list.append(5)
        elif numb == 'SIX':
            int_list.append(6)
        elif numb == 'SVN':
            int_list.append(7)
        elif numb == 'EGT':
            int_list.append(8)
        elif numb == 'NIN':
            int_list.append(9)

    return int_list


def change2Str(int_list, string_list):
    for numb in int_list:
        if numb == 0:
            string_list.append('ZRO')
        elif numb == 1:
            string_list.append('ONE')
        elif numb == 2:
            string_list.append('TWO')
        elif numb == 3:
            string_list.append('THR')
        elif numb == 4:
            string_list.append('FOR')
        elif numb == 5:
            string_list.append('FIV')
        elif numb == 6:
            string_list.append('SIX')
        elif numb == 7:
            string_list.append('SVN')
        elif numb == 8:
            string_list.append('EGT')
        elif numb == 9:
            string_list.append('NIN')

    return string_list

T = int(input())

for tc in range(1, T + 1):
    tc_numb, length = input().split()

    str_arr = list(input().split())
    str_to_int = change2Int(str_arr, [])

    str_to_int.sort()

    sorted_str = change2Str(str_to_int, [])
    print(f'#{tc} ', end='')
    print(*sorted_str)



