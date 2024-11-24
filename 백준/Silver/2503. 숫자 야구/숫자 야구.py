'''
1. A가 정답으로 생각할 수 있는 모든 수 넣어보기
2. B가 도전한 내용이 맞는지 확인하기
'''

import sys
input = sys.stdin.readline

n = int(input())
number_list = [list(input().split()) for _ in range(n)]
range_num = list(str(i) for i in range(1, 10))
ans = 0
for a in range_num:
    for b in range_num:
        for c in range_num:
            if (a == b or b == c or c == a):
                continue
            hint = 0
            # 숫자가 정해진 경우 진행
            for arr in number_list:
                number, strike, ball = arr

                strike_cnt = 0
                ball_cnt = 0

                # 스트라이크 체크
                if a == number[0]:
                    strike_cnt += 1
                if b == number[1]:
                    strike_cnt += 1
                if c == number[2]:
                    strike_cnt += 1

                # 볼 체크
                if (a == number[1] or a == number[2]):
                    ball_cnt += 1
                if (b == number[0] or b == number[2]):
                    ball_cnt += 1
                if (c == number[0] or c == number[1]):
                    ball_cnt += 1


                if int(ball) == ball_cnt and int(strike) == strike_cnt:
                    hint += 1
            if hint == n:
                ans += 1

print(ans)