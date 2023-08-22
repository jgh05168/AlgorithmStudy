first = int(input())
n = first

max_cnt = 0
max_lists = []
for i in range(n + 1):
    cnt = 2
    before = first
    after = first - i
    lists = [before, after]
    while True:
        next = before - after
        if next < 0:
            if max_cnt < cnt:
                max_cnt = cnt
                max_lists = lists
            break
        else:
            lists.append(next)
            cnt += 1
            before = after
            after = next

print(max_cnt)
print(*max_lists)