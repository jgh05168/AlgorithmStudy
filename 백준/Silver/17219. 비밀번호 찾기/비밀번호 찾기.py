N, M = map(int, input().split())

dict = {}
for _ in range(N):
    site, password = input().split()
    dict.update({site: password})

for _ in range(M):
    findsite = input()
    if findsite in dict.keys():
        print(dict[findsite])