'''
문자열 폭발

그리디 알고리즘 -> 시간초과

스택을 사용한다.
    - 현재 문자열과 key의 끝 값을 계속 비교한다. -> 다르다면 계속 스택에 삽입
    - 비교했을 때 현재 문자열과 끝 값이 같다면, 슬라이싱을 사용하여 폭발 문자와 같은지 확인
    - 같다고 판별되었으면 길이만큼 pop 
'''

string = list(input())
key = list(input())

check = 0

new_string = []
for c in range(len(string)):
    new_string.append(string[c])
    if string[c] == key[-1]:
        if new_string[len(new_string) - len(key):] == key:
            for _ in range(len(key)):
                new_string.pop()

if not len(new_string):
    print('FRULA')
else:
    print(''.join(list(new_string)))