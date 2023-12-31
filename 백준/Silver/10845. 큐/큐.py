from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
queue = deque()
for _ in range(n):
    order = list(input().split())

    if len(order) == 2:
        queue.append(int(order[1]))
    else:
        if order[0] == 'pop':
            if not queue:
                print(-1)
            else:
                print(queue.popleft())
        elif order[0] == 'size':
            print(len(queue))
        elif order[0] == 'empty':
            if not queue:
                print(1)
            else:
                print(0)
        elif order[0] == 'front':
            if not queue:
                print(-1)
            else:
                print(queue[0])
        elif order[0] == 'back':
            if not queue:
                print(-1)
            else:
                print(queue[-1])