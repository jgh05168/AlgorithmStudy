
switch = int(input())

switch_list = list(map(int, input().split()))

students = int(input())

for student in range(students):
    gender, number = map(int, input().split())

    if gender == 1:
        for i in range(number - 1, switch, number):
            if switch_list[i] == 1:
                switch_list[i] = 0
            else:
                switch_list[i] = 1
    elif gender == 2:
        if switch_list[number - 1] == 1:
            switch_list[number - 1] = 0
        else:
            switch_list[number - 1] = 1
        for j in range(1, switch - number + 1):
            if 0 <= number - j - 1 and switch > number + j - 1:
                if switch_list[number - j - 1] == switch_list[number + j - 1]:
                    if switch_list[number - j - 1] == 0:
                        switch_list[number - j - 1], switch_list[number + j - 1] = 1, 1
                    else:
                        switch_list[number - j - 1], switch_list[number + j - 1] = 0, 0
                else:
                    break
            else:
                break

cnt = 1
for i in range(switch):
    if i == 20 * cnt - 1:
        cnt += 1
        print(switch_list[i])
    else:
        print(switch_list[i], end=' ')

