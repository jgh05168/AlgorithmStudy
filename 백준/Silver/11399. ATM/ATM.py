N = int(input())
line = list(map(int, input().split()))

# 정렬 후 문제의 방법대로 더하기 
line.sort()
val = 0
total = 0
for i in line:
    val += i
    total += val
print(total)