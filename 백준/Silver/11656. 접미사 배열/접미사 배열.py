S = input()

output = []

start = 0
for c in range(len(S)):
    new_arr = []
    for i in range(start, len(S)):
        new_arr.append(S[i])
    start += 1
    output.append(''.join(new_arr))

for i in sorted(output):
    print(i)

