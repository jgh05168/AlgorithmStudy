
N = int(input())

# N을 7로 나누었을 때 나머지가 2 또는 0일 경우 창영이가 승리한다.
# 아닌경우, 무조건 상근이가 이겨
if N % 7 == 0 or N % 7 == 2:
    print('CY')
else:
    print('SK')