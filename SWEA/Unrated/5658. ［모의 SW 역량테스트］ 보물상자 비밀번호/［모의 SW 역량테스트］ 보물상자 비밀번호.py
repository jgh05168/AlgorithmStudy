dict = {'1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
        '6': '0110', '7': '0111', '8': '1000', '9': '1001',
        'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    hex_number = list(input())
    secret_codes = set()

    for i in range(N // 4):
        # 비밀번호 돌리기
        rotate = list(hex_number.pop())
        rotate.extend(hex_number)
        hex_number = rotate

        # 가능한 비밀번호 저장
        for j in range(0, N, N // 4):
            secret_code = []
            for k in range(j, j + (N // 4)):
                secret_code.append(hex_number[k])
            secret_codes.add(''.join(secret_code))

    # 16진수를 10진수로 변환
    dec_codes = {}
    for hex_code in secret_codes:
        dec_codes.update({int(hex_code, 16): hex_code})

    # 내림차순으로 정렬
    dec_codes = sorted(dec_codes.items(), key=lambda x:x[0], reverse=True)

    # 큰 수 찾기
    print(f'#{tc} {dec_codes[K - 1][0]}')