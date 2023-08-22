
N = int(input())

# 최대 가로 길이를 갖는 리스트 초기화
cabin = [0] * 1001
for _ in range(N):
    store_l, store_h = map(int, input().split())
    cabin[store_l] = store_h        # 기둥의 높이를 1로 하여 리스트에 저장

# 최대 높이 기둥의 인덱스 번호를 찾는 과정
max_height = 0
max_h_length = 0
for idx, height in enumerate(cabin):
    if max_height < height:
        max_h_length = idx
        max_height = height

# 최대높이기둥 인덱스를 기준으로 왼쪽과 오른쪽으로 나누어서 탐색
# 왼쪽(처음부터 최대 기둥 방향)
width = 0
left = 0
for i in range(max_h_length + 1):
    if cabin[i] and left < cabin[i]:
        left = cabin[i]
    width += left
    
# 오른쪽(마지막부터 최대 기둥 방향)
right = 0
for i in range(len(cabin) - 1, max_h_length, -1):
    if cabin[i] and right < cabin[i]:
        right = cabin[i]
    width += right
print(width)
