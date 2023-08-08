T = 10

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(input()) for _ in range(8)]
    cnt = 0

    # 8 by 8 행렬에 대해 반복해서 순회
    for i in range(8):
        start = 0
        for j in range(start, 8 - N + 1):
            rword = ""
            cword = ""
            for k in range(N):      # 알고자하는 단어의 길이 만큼 알파벳을 조합해 단어 생성
                rword += arr[i][j + k]      # 시작 인덱스 : j (0, 1, ... , 8 - 알고자 하는 단어 길이 + 1)
                cword += arr[j + k][i]

            rev_rword = ""
            rev_cword = ""
            # 단어 reverse 수행(인덱스)
            # 후에 문제 풀 때는 슬라이싱이 편하긴 하니 슬라이싱 써야지
            for c in range(N - 1, -1, -1):
                rev_rword += rword[c]
                rev_cword += cword[c]

            # 회문이 존재하는지 확인 후 개수 세기
            if rword == rev_rword:
                cnt += 1
            if cword == rev_cword:
                cnt += 1

    print(f'#{tc} {cnt}')


