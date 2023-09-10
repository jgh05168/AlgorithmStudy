T = int(input())

for _ in range(T):
    R, S = input().split()
    P = ''
    for i in range(len(S)):
        for _ in range(int(R)):
            P += S[i]
    print(P)