from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
order = list(map(int, input().split()))
order.reverse()
init_deck = deque()
last_deck = list(reversed([i for i in range(1, n + 1)]))

for i in range(n):
    number = last_deck.pop()
    if order[i] == 1:
        init_deck.append(number)
    elif order[i] == 2:
        init_deck.insert(-1, number)
    else:
        init_deck.appendleft(number)

init_deck.reverse()
print(*init_deck)