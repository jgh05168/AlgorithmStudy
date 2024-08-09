'''
두 문자열 S와 T가 주어졌을 때, S를 T로 바꾸는 게임

- 문자열의 뒤에 A를 추가한다.
- 문자열을 뒤집고 뒤에 B를 추가한다.

풀이:
list 안에서 꺼내가면서 연산 해보기
bfs 처럼 진행
길이보다 커지면 종료
----------------- 메모리 초과
뒤에서부터 없애가면서 시작해보기
- 두 조건 모두 뒤에 'A' or 'B'를 추가해야 한다.
- 둘 중에 하나만 무조건 나올 것이다. 
-> 'B'면 reverse, 'A'면 그대로 진행
'''

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while T:
    last_t = T.pop()
    if last_t == 'B':
        T.reverse()
    if T == S:
        print(1)
        exit()
print(0)