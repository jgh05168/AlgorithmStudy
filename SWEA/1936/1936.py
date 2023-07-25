A, B = map(int, input().split())

if (A > 3 or A < 0 or B > 3 or B < 0):
    exit()
elif (A == B):
    exit()

if (A > B):
    if (B == 1 and A == 3):
        print("B")
    else:
        print("A")
elif (B > A):
    if (A == 1 and B == 3):
        print("A")
    else:
        print("B")
