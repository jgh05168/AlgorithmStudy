
def check(word):
    char_list = []
    groupword = True
    for char in word:
        if char in char_list:
            if char != char_list[-1]:
                groupword = False
                break
        else:
            char_list.append(char)

    return groupword


N = int(input())

if N < 0 or N > 100:
    quit()

cnt = 0
for test_case in range(1, N + 1):
    input_word = input()
    
    

    if check(input_word) == True:
        cnt += 1

print(cnt)


    