n = int(input())
string = list(input())
cnt = 0

for i in range(n):
    if string[i] in ('a', 'e', 'i', 'o', 'u'):
        cnt += 1

print(cnt)