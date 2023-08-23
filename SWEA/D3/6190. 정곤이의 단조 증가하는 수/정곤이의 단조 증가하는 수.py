
# 재귀함수
def rec(n):
    global startval
    if n <= 0:  # 모두 다 탐색하였다면 1 반환
        return 1
    else:
        if startval >= n % 10:      # 현재 자리값이 startval보다 작거나 같으면 = 단조 증가하는 수
            startval = n % 10       # startval 업데이트
            return rec(n // 10)     # 10으로 나눈 몫값을 업데이트
        else:
            return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(input().split())
    d_list = []
    length = 0
    # 단조 찾기
    for i in range(N - 1):
        for j in range(i + 1, N):
            d = int(A[i]) * int(A[j])
            d_list.append(d)


    getdanjo = [0] * len(d_list)

    # 각각 찾은 숫자리스트들이 단조 증가하는 수인지 아닌지 확인
    for d in range(len(d_list)):
        # 1의자리 수라면, 단조 증가를 볼 필요가 없으므로 저장
        if d_list[d] // 10 == 0:
            getdanjo[d] = d_list[d]
        else:
            # 1의 자리수부터 자릿수를 증가시키면서 비교
            startval = 9        # 가장 큰 값 설정
            check = rec(d_list[d])
            if check:
                getdanjo[d] = d_list[d]

    if max(getdanjo) == 0:
        print(f'#{tc} {-1}')
    else:
        print(f'#{tc} {max(getdanjo)}')