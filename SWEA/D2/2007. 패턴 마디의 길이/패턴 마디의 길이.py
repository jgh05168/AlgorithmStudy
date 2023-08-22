T = int(input())

for tc in range(1, T + 1):
    string = input()
    c_list = []     # 단어를 완성하기 위해 저장하는 역할의 list
    c = 0           # index 넘버
    
    while c < 30:
        make = False
        # 만약 현재 단어가 c_list에 없다면 : 단어가 완성되지 않은 것임
        if string[c] not in c_list:
            c_list.append(string[c])    # list에 추가
            c += 1                      # 단어 인덱스 + 1
        else:       # 단어가 존재한다면
            # 현재 단어 이후에 대해서 c_list와 현재 위치의 string이 같은지 비교
            for idx in range(1, len(c_list)):       
                # 만약 idx + c가 범위 내에 존재하고, 이후의 단어들이 다르다면 : 단어가 더 있다는 뜻이다.
                if idx + c < 30 and c_list[idx] != string[idx + c]:
                    c_list.append(string[c])        # c_list에 단어 추가
                    c += 1                          # 단어 인덱스 + 1
                    break
            else:       # for-else 문을 통해 만약 break 없이 for 문을 다 순회하였다면
                make = True     # 단어가 다 왼성되었다.
        
        # 만약 단어가 다 완성되었다면, 반복문을 빠져나온다.
        if make:
            break
            
    print(f'#{tc} {len(c_list)}')