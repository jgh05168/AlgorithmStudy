'''
각 염색체가 규칙을 만족하는지 검사하기

- 문자열은 ABCDEF 중 0개 or 1개 존재해야함
- 그 다음 문자열은 A가 무조건 있어야 한다.
- 그 다음에는 F가 무조건 있어야 한다.
- 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
- 나머지는 ABCDEF 중 하나가 있다.

규칙을 지키는 경우는 Infected!, 아니면 Good

풀이: 일단 초반이 ABCDEF인 지 확인하기
그리고 규칙을 지키는지 확인하기
'''

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    input_string = input().rstrip()

    flag = 0
    start = 0
    tmp_idx = 0
    if input_string[0] in ['A', 'B', 'C', 'D', 'E', 'F']:
        tmp_idx = 1
    else:
        flag = 1

    if not flag:
        # 2. 두 번 째
        for idx in range(tmp_idx, len(input_string)):
            if input_string[idx] == 'F':
                tmp_idx = idx
                break
            elif input_string[idx] == 'A':
                continue
            else:
                flag = 1

    if not flag:
        # 세 번 째
        for idx in range(tmp_idx, len(input_string)):
            if input_string[idx] == 'C':
                tmp_idx = idx
                break
            elif input_string[idx] == 'F':
                continue
            else:
                flag = 1

    if not flag:
        # 네 번 째
        for idx in range(tmp_idx, len(input_string)):
            if input_string[idx] in ['A', 'B', 'C', 'D', 'E', 'F']:
                tmp_idx = idx
                break
            elif input_string[idx] == 'C':
                continue
            else:
                flag = 1

    if not flag:
        # 마지막
        for idx in range(tmp_idx, len(input_string)):
            if input_string[idx] in ['A', 'B', 'C', 'D', 'E', 'F']:
                continue
            else:
                flag = 1

    if flag:
        print("Good")
    else:
        print("Infected!")