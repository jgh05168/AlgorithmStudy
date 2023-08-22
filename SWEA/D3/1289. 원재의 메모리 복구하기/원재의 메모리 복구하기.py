T = int(input())

for tc in range(1, T + 1):
    memory = list(map(int, input()))

    # 초기상태 제공
    zero_bit = list([0] * len(memory))
    cnt = 0
    for bit in range(len(memory)):
        if memory[bit] != zero_bit[bit]:
            val = bit
            # 0이라면 1로, 1이라면 0으로 끝까지 변환
            if zero_bit[bit] == 0:
                while val < len(memory):
                    zero_bit[val] = 1
                    val += 1
            else:
                while val < len(memory):
                    zero_bit[val] = 0
                    val += 1
            cnt += 1

    print(f'#{tc} {cnt}')