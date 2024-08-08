'''
슬라이딩 윈도우 사용
잘라서 체크해보기
'''

from collections import deque
import sys
input = sys.stdin.readline

s, p = map(int, input().split())
dna = list(input().rstrip())
counts = list(map(int, input().split()))
A, C, G, T = 0, 0, 0, 0
ans = 0

def add(ch):
    global A, C, G, T
    if ch == 'A':
        A += 1
    elif ch == 'C':
        C += 1
    elif ch == 'G':
        G += 1
    elif ch == 'T':
        T += 1

def sub(ch):
    global A, C, G, T
    if ch == 'A':
        A -= 1
    elif ch == 'C':
        C -= 1
    elif ch == 'G':
        G -= 1
    elif ch == 'T':
        T -= 1

sub_dna = deque([0] + dna[0:p - 1])
for j in range(p):
    add(sub_dna[j])

sub_p = p - 1
for i in range(s - p + 1):
    start, end = sub_dna.popleft(), dna[sub_p]
    sub(start)
    add(end)
    sub_dna.append(end)
    sub_p += 1
    if A < counts[0] or C < counts[1] or G < counts[2] or T < counts[3]:
        continue
    ans += 1

print(ans)