'''
10836 여왕벌

m x m
애벌레들은  매일 에너지를 모아서 정오에 자라는데, 무시가  가능함
이 과정을 n일동안 반복
크기가 커지는 과정
1. 제일 왼쪽 열, 제일 위쪽 행 애벌레들은 자신이 자라는 정도를 스스로 결정한다.
    - 자라는 정도를 왼쪽 제일 아래 칸부터 위로가면서 읽고, 위에 도착하면 오른쪽으로 가면서 읽는다.
2. 나머지 애벌레들은 자신의 왼, 왼위, 위 애벌레들의 정도를 파악한 후, 그 날 가장 많이 자란 애벌레가 자란 만큼 자란다.

풀이:
N < 1000000
규칙을 찾아서 마지막에 더해주는 방식으로 가야한다.
- 백만번 입력 받아서 배열에 누적한 뒤, 배열 업데이트 해주는 방식
-> 14억 .. 시초
=> 이를 해결하기 위해 구간을 나누어 값 업데이트(0, 1, 2)
'''

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    M, N = map(int, input().split())  # M: 가로와 세로 크기, N: 날짜 수
    larva = [1 for _ in range(2 * M - 1)]  # 애벌레의 크기

    for _ in range(N):
        zero, one, two = map(int, input().split())

        for i in range(zero, zero + one):  # 애벌레 크기 1만큼 증가
            larva[i] += 1

        for i in range(zero + one, zero + one + two):  # 애벌레 크기 2만큼 증가
            larva[i] += 2

    # 제일 왼쪽 열과, 제일 위쪽 행의 애벌레는 입력으로 주어진 만큼 커진다.
    # 나머지 애벌레는 항상 자신의 위쪽 애벌레만큼 크기가 커지게 된다.
    # 따라서 [i][j] (i >= 1, j >= 1) 위치의 애벌레는 항상 [0][j]의 애벌레의 크기와 같다.
    for i in range(M):
        for j in range(M):
            if j == 0:
                print(larva[M - (i + 1)], end=' ')
            else:
                print(larva[M + j - 1], end=' ')
        print()


'''
dp로도 해결 가능함
1. n만큼 반복문 돌기
    - 0, 1, 2만큼 값을 증가시킬 수 있으므로, 1과 2 값 증가가 시작하는 부분에 +1을 진행해준다.
2. dp 돌면서 이전에 저장한 값의 1이 증가했다면, cnt++ 로 값 증가시키며 업데이트하기

import sys
input = sys.stdin.readline

def grow(p, M):
    dp = [[1 for _ in range(M)] for _ in range(M)]
    r, c = M - 1, 0
    cnt = 0
    for i in range(2 * M - 1):
        cnt += p[i]
        dp[r][c] += cnt
        if r != 0:
            r -= 1
        else:
            c += 1

    return dp

def solution():
    M, N = map(int, input().split())
    p = [0 for _ in range(2 * M - 1)]
    for _ in range(N):
        tmp = tuple(map(int, input().split()))
        idx = 0
        for i in range(3):
            idx += tmp[i]
            if idx >= 2 * M - 1:
                break
            p[idx] += 1

    dp = grow(p, M)

    for i in range(1, M):
        for j in range(1, M):
            if (i, j) == (1, 1):
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    for row in dp:
        print(*row)

solution()
'''
