K = int(input())

llist = []
cnt_list = [0] * 4
max_length, sub_length = 0, 0
max_height, sub_height = 0, 0

# 큰 넓이에서 비는 넓이를 빼서 계산
for i in range(6):
    dir, val = map(int, input().split())
    llist.append((dir, val))
    cnt_list[dir - 1] += 1

# 하나만 있는 인덱스 찾기
max_idx = []
for i in range(4):
    if cnt_list[i] == 1:
        max_idx.append(i + 1)

# 조건을 찾아야한다
# 4 2 1 3 1 3 에서 4 2가 최대 길이, 최대 넓이라면
# 나머지 작은 부분은 1 3 1 3  중 가운데 3 1의 값이다.

# 이와 같은 규칙을 만족함
while True:
    idx, val = llist.pop(0)
    if idx in max_idx:
        if llist[0][0] not in max_idx:
            idx2, val2 = llist.pop()
        else:
            idx2, val2 = llist.pop(0)
        max_width = val * val2

        llist.pop(0)
        sub_idx1, sub_val1 = llist.pop(0)
        sub_idx2, sub_val2 = llist.pop(0)
        sub_width = sub_val1 * sub_val2
        break
    else:
        llist.append((idx, val))

print((max_width - sub_width) * K)
