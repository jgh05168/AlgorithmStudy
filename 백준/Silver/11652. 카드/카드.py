import sys
input = sys.stdin.readline

n = int(input())

dictionary = {}
for _ in range(n):
    x = int(input())
    if x in dictionary.keys():
        dictionary[x] += 1
    else:
        dictionary.update({x: 1})

max_val = 0
ans = (0, 0)
for key, value in dictionary.items():
    if max_val < value:
        ans = (value, key)
        max_val = value
    elif max_val == value:
        if ans[1] > key:
            ans = (value, key)

print(ans[1])