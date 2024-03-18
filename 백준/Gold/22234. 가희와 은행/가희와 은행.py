'''
대기줄 손님 N명

x번 손님 정보는 id값인 Px와 업무를 처리하는데 필요한 시간 tx 정보 주어짐

시작하고 난 후 M명이 들어온다.
    - Px와 Tx, 영업시작 cx초 후에 들어왔다 는 정보 주어짐
들어옴과 동시에 큐에 들어온다.

1. tx가 T보다 크면 x번 손님의 업무를 T초동안 처리. 그 후 tx는 T만큼 감소
2. 그렇지 않으면 x번 손님의 업무를 tx동안 처리. 이 때 손님의 tx는 0
3. tx가 0이 되면 탈출
4. 그렇지 않으면 대기큐의 맨 뒤로 이동. 만약 도착한 손님이 있다면(우선순위 높음) 그 뒤로 간다.
5.대기 큐에 고객이 남았다면 1로 돌아간다.

0 ~ W - 1초가 지날 때까지 창구에 있는 직원이 어떤 고객의 업무ㅡㄹ 처리하는지 말해줘

풀이 : 그냥 deck 같은데 ..

'''

from collections import deque
import sys
input = sys.stdin.readline

n, t, w = map(int, input().split())
deck = deque()
wait_deck = []
for _ in range(n):
    px, tx = map(int, input().split())
    deck.append((px, tx))
m = int(input())
# 얘네는 time이 맞다면 pop 후 대기줄에 껴주기
for _ in range(m):
    px, tx, cx = map(int, input().split())
    wait_deck.append((px, tx, cx))

wait_deck.sort(key=lambda x: x[2])      # 기다린 시간만큼 앞에 서야하므로 오름차순 처리 해줌
wait_deck = deque(wait_deck)

time_sum = 0
for time in range(w):
    cur_p, cur_t = deck.popleft()
    print(cur_p)
    time_sum += 1
    while wait_deck and wait_deck[0][2] == time + 1:       # 만약 맨처음 기다리는 사람의 순서가 되었다면, 대기줄에 껴주기
        tp, tc, cc = wait_deck.popleft()
        deck.append((tp, tc))
    if time_sum == t and cur_t > t:
        deck.append((cur_p, cur_t - time_sum))
        time_sum = 0
    elif cur_t - time_sum:
        deck.appendleft((cur_p, cur_t))
    else:
        time_sum = 0
