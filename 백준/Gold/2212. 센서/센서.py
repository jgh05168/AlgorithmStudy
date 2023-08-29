
N = int(input())
K = int(input())
# 집중국을 한 집 당 하나씩 쓸 수 있는 경우
if N <= K:
    print(0)

else:
    # 좌표별로 오름차순 정렬
    highway = sorted(list(map(int, input().split())))

    adj_len = [0] * (N - 1)
    # 센서 간의 거리 계산
    for i in range(1, N):
        adj_len[i - 1] = highway[i] - highway[i - 1]

    # 거리가 먼 순부터 없애야 하므로 오름차순 정렬(뒤에서부터 처리할 것이기 떄문)
    adj_len.sort()
    # 거리가 먼 순으로 K - 1만큼 집중국 연결을 끊어준다.
    # (총 K개의 집중국을 사용하기 때문)
    # 이후 최단 거리들을 모두 더해준다.
    print(sum(adj_len[:N - K]))
