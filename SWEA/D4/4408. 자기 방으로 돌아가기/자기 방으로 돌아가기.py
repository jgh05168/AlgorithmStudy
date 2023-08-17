T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    students = []
    for _ in range(N):
        cur, dir = map(int, input().split())
        students.append((cur, dir))

    floors = [0] * (200 + 1)        # 복도는 하나이므로 400 // 2 + 1로 설정
    # 겹치는 부분은 원래 값 + 1
    # 어차피 겹치지 않는 시간은 한번에 이동하기 떄문에 floor의 최대값이 최소단위시간이다.
    # % 2 == 0 / 1 로 인덱스넘버를 확인

    for student in students:
        room1, room2 = 0, 0
        
        if student[0] % 2 == 1:
            room1 = student[0] // 2 + 1
        elif student[0] % 2 == 0:
            room1 = student[0] // 2

        if student[1] % 2 == 1:
            room2 = student[1] // 2 + 1
        elif student[1] % 2 == 0:
            room2 = student[1] // 2

        if room1 < room2:
            for i in range(room1, room2 + 1):
                floors[i] += 1
        else:
            for j in range(room2, room1 + 1):
                floors[j] += 1

    print(f'#{tc} {max(floors)}')