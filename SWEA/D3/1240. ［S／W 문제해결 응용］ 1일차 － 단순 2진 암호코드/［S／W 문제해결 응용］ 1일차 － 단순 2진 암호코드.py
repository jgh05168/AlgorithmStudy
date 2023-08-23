
T = int(input())

for tc in range(1, T + 1):
    dict = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011',
            5: '0110001', 6: '0101111', 7: '0111011', 8: '0110111', 9: '0001011'}
    N, M = map(int, input().split())

    secret_list = [list(map(int, input())) for _ in range(N)]
    secret_code = []
    for row in range(N - 1, -1, -1):
        for col in range(M - 1, -1, -1):
            if secret_list[row][col] == 1:
                secret_code = secret_list[row][col:col - 56:-1]
                break
    secret_code = [0] + secret_code
    get_code = []
    for i in range(56, 0, -7):
        bit = secret_code[i: i - 7: -1]
        for i in range(len(bit)):
            bit[i] = str(bit[i])
        for key, val in dict.items():
            if val == ''.join(bit):
                get_code.append(key)

    odd = 0
    even = 0
    for i in range(len(get_code)):
        if i % 2 == 0:
            odd += get_code[i]
        else:
            even += get_code[i]

    output = 0
    if (odd * 3 + even) % 10 == 0:
        for code in get_code:
            output += code
        print(f'#{tc} {output}')
    else:
        print(f'#{tc} {0}')

