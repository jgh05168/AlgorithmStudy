def hanoi(n, start, end, save):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, save ,end)
    print(start, end)
    hanoi(n-1, save, end, start)


N = int(input())
print(2**N-1)
if N <= 20:
    hanoi(N,1,3,2)