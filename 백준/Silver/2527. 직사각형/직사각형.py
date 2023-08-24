
for _ in range(4):
    points = list(map(int, input().split()))
    x1, y1, p1, q1 = points[:4]
    x2, y2, p2, q2 = points[4:]
    # 점
    if ((x1, y1) == (p2, q2) or (p1, q1) == (x2, y2) or
            (p1, y1) == (x2, q2) or (x1, q1) == (p2, y2)):
        print('c')
    # 공통부분 x
    elif x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        print('d')
    # 선분
    elif p1 == x2 or x1 == p2 or y1 == q2 or y2 == q1:
        print('b')
    # 직사각형
    else:
        print('a')