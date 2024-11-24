import sys
input = sys.stdin.readline

n = int(input())
ans = 0
for a in range(n + 1):
    for b in range(n + 1):
        for c in range(n + 1):
            if a + b + c == n and a >= b + 2 and a and b and c and not c % 2:
                ans += 1

print(ans)