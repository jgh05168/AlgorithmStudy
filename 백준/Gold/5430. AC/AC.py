'''
정수 배열에 연산을 하기 위함.
R뒤집기 : 배열에 있는 수의 순서를 뒤집는 함수
D버리기 : 첫번째 수를 버리는 함수
    - 배열이 비어있는 경우 사용하면 에러 발생

스택, 큐를 사용해서 다 해보자

추가) R 이 주어질 때마다 reverse를 하면 시간초과 발생.
    -> reverse boolean을 생성해주어 결과를 출력할 때 한 번만 reverse 진행
+ 문자열 인덱싱, 슬라이싱 등 파이썬의 기능을 잘 활용하자
'''

from collections import deque
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    funcs = list(input().rstrip())
    n = int(input())
    lists = input().rstrip()[1:-1].split(',')
    lists = deque(lists)


    reverse = False
    error = False
    if not n:
        lists = deque()
    for func in funcs:
        if func == 'R':    # 뒤집기
            if reverse:
                reverse = False
            else:
                reverse = True

        else:       # 첫번째 수 버리기
            if lists == deque():
                error = True
                print('error')
                break
            if not reverse:
                lists.popleft()
            else:
                lists.pop()

    # 출력부분
    if not error:
        if reverse:
            lists.reverse()
            print('[' + ','.join(lists) + ']')
        else:
            print('[' + ','.join(lists) + ']')

