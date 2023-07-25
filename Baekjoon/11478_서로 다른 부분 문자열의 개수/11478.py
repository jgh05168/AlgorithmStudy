S = input()

result = set()
for i in range(1,len(S)+1):
    for x in range(len(S) + 1 - i):
        result.add(S[x:x+i])

print(len(result))