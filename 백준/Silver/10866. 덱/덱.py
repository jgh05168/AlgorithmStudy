'''
덱 구현
'''

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
deck = deque()

for _ in range(n):
    order = list(input().split())

    if order[0] == 'push_front':
        deck.appendleft(int(order[1]))
    elif order[0] == 'push_back':
        deck.append(int(order[1]))
    elif order[0] == 'pop_front':
        if deck:
            print(deck.popleft())
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if deck:
            print(deck.pop())
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(deck))
    elif order[0] == 'empty':
        if deck:
            print(0)
        else:
            print(1)
    elif order[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print(-1)
    else:
        if deck:
            print(deck[-1])
        else:
            print(-1)
