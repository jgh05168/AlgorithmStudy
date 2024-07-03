'''
DSLR
1. D : n을 두 배로 바꾼다. 값이 9999보다 크면  10000으로 나눈 나머지를 저장
2. S : n에서 1을 뺀 결과(n-1). n이 0이라면, 9999가 대신 저장
3. L : 왼편으로 회전.
4. R : 오른편으로 회전

풀이 : bfs

----- 시간초과 -----
    구조체를 queue에 넣어서 생각함.
    deque 사용해서 큐를 돌려 정보를 저장했더니 시간초과가 난다.

----- 해결법 -----
    수학적으로 풀어나가자.
    D, S, L, R을 수학적 수식으로 생각하기
    이렇게 처리하니 정답.
    visited는 배열 인덱스로 하든, set() 사용하던 상관없다.
        -> 어차피 시간복잡도 O(1)
'''

from collections import deque
import sys
input = sys.stdin.readline

codes = ['D', 'S', 'L', 'R']

def bfs(a):
    global final_order
    queue = deque()
    visited.add(a)
    queue.append((a, ""))        # 현재 폼, 이동한 거리

    while queue:
        cur_a, order= queue.popleft()

        for d in range(4):
            if codes[d] == 'D':
                new_a = (cur_a * 2) % 10000
                if new_a not in visited:
                    if new_a == b:
                        final_order = order + 'D'
                        return
                    visited.add(new_a)
                    queue.append((new_a, order + "D"))
            elif codes[d] == 'S':
                new_a = (cur_a - 1) % 10000
                if new_a not in visited:
                    if new_a == b:
                        final_order = order + 'S'
                        return
                    visited.add(new_a)
                    queue.append((new_a, order + "S"))
            elif codes[d] == 'L':
                new_a = cur_a // 1000 + (cur_a % 1000) * 10
                if new_a not in visited:
                    if new_a == b:
                        final_order = order + 'L'
                        return
                    visited.add(new_a)
                    queue.append((new_a, order + "L"))
            else:
                new_a = cur_a // 10 + (cur_a % 10) * 1000
                if new_a not in visited:
                    if new_a == b:
                        final_order = order + 'R'
                        return
                    visited.add(new_a)
                    queue.append((new_a, order + "R"))

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    final_order = ""
    min_cnt = int(1e9)
    visited = set()
    bfs(a)

    print(final_order)
