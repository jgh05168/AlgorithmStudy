'''
공주님의 정원

3월 1일 ~ 11월 30일까지 매일 꽃이 한 가지 이상 피어있도록 한다
꽃의 최소 개수를 출력

풀이:
정렬 필수
1. 일 로 통일시키기
2. <10만 이므로 한번에 쭉 가야한다.
    - 만약 겹치는 날이 있으면, 최대한 날짜 길게 늘이기
3. 11월 30일보다 늦은 날짜가 나오면 종료
'''

from collections import defaultdict, deque
import sys
input = sys.stdin.readline

days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
calendar = defaultdict(int)
for i in range(1, 13):
    calendar[i] = calendar[i - 1] + days[i - 1]


n = int(input())
bef_flowers = []
flowers = []
start, end = calendar[3] + 1, calendar[11] + 30
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    sd, ed = calendar[sm] + sd, calendar[em] + ed - 1
    if sd <= start:
        bef_flowers.append((sd, ed))
    else:
        flowers.append((sd, ed))


# 3월 1일 전까지는 최대한 늦게 지는 애들을 택하는 것이 좋다.
bef_flowers.sort(key=lambda x: -x[1])
if not bef_flowers:
    print(0)
    exit()
now_rise = deque([bef_flowers[0][0]])
now_fall = deque([bef_flowers[0][1]])

# 만약 바로 끝날 수 있는 경우라면
if now_fall[-1] >= end:
    print(1)
    exit()

# 이후 애들은 순회하면서 피는 날짜 사이에 존재한다면 끝나는 날 늦은 걸로 업데이트하기
ans = 0
flowers.sort(key=lambda x: (x[0], -x[1]))
for i in range(len(flowers)):
    # 생각해야 할 조건
    # 1. 현재 끝나는 날짜보다 시작 날짜가 시작 전인가 ?
    # 2. 끝나는 날짜가 현재 날짜보다 늦는가 ?
    sd, ed = flowers[i]
    # 아직 날짜가 끝나지 않고 이어갈 수 있는가 ?
    # 1번 조건
    if sd <= now_fall[0] + 1:
        # 2번 조건
        if ed > now_fall[-1]:
            if len(now_fall) > 1:
                now_fall.pop()
                now_rise.pop()
            now_fall.append(ed)
            now_rise.append(sd)
    # 만약 현재 꽃이 다 졌다면 ?
    else:
        last_fall = 0
        while now_fall and sd > now_fall[0]:
            ans += 1
            last_fall = now_fall.popleft()
            now_rise.popleft()
        if not now_rise and last_fall + 1 == sd:
            now_fall.append(ed)
            now_rise.append(sd)
        elif now_fall and sd <= now_fall[0] + 1 and now_fall[-1] < end:
            now_fall.append(ed)
            now_rise.append(sd)
        if not now_rise:
            ans = 0
            break


if now_fall and now_fall[-1] < end:
    ans = 0
else:
    while now_fall:
        ans += 1
        now_fall.pop()
        now_rise.pop()
print(ans)

