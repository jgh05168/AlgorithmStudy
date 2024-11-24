n = int(input())
for _ in range(n):
    s = int(input())
    for m in range(2, 1000000):
        if not s % m:
            print("NO")
            break
    else:
        print("YES")