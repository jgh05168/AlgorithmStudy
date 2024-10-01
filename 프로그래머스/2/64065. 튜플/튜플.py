'''
풀이:
1. 입력을 하나씩 순차적으로 받기
2. 순서대로 튜플에 담기.
'''
'''
풀이:
1. 입력을 하나씩 순차적으로 받기
2. 순서대로 튜플에 담기.
'''

def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)
    
    answer_set = set()
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer_set:
                answer.append(int(i[j]))
                answer_set.add(int(i[j]))

    return answer

