'''
풀이:
1. 입력을 하나씩 순차적으로 받기
2. 순서대로 튜플에 담기.
'''
def solution(s):
    answer = []

    s = list(s.split(','))
    s_list = []
    tmp_list = []
    tmp_s = ''
    close = 1
    for ss in s:
        for c in ss:
            if c == '{':
                close = 0
            elif c.isdigit() and not close:
                tmp_s += c
            elif c == '}':
                if tmp_s != '':
                    tmp_list.append(tmp_s)
                    tmp_s = ''
                if tmp_list:
                    s_list.append(tmp_list)
                    tmp_list = []
                close = 1
        if not close:
            tmp_list.append(tmp_s)
            tmp_s = ''
    
    s_list.sort(key=lambda x: len(x))
    
    comb_set = set()
    for s in s_list:
        for i in s:
            if i not in comb_set:
                comb_set.add(i)
                answer.append(int(i))
                break

    return answer