'''
N-Queen

- 체스판을 그대로 구현하여 시뮬레이션처럼 풀려고 한다면 시간초과가 발생한다.
- row 라는 1차원 배열을 생성해주어, row의 값에다 col 정보를 저장한다.

갈 수 없는 조건
    1. 이전에 놓았던 queen들 중 같은 열에 있는 queen이 존재하는 경우
    2. 대각선에서 걸리는지 판단. => abs(row[player] - row[i]) == abs(player - i)
        여기서 i는 현재 몇 개의 queen 이 놓여있는 지를 반복해보기

'''

def is_possible(player):
    for i in range(player):
        # 갈 수 없는 조건
        if row[player] == row[i] or abs(row[player] - row[i]) == abs(player - i):
            return False
    return True

def nqueen(player):
    global cnt
    # 종료 조건
    if player >= N:
        cnt += 1
        return
    for i in range(N):
        row[player] = i
        if is_possible(player):
            nqueen(player + 1)


N = int(input())
row = [0] * N
cnt = 0
nqueen(0)

print(cnt)