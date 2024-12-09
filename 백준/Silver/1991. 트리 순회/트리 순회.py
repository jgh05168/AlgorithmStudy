def preOrder(start):
    if start != -18:
        print(chr(start+64), end="")
        preOrder(tree[start][0])
        preOrder(tree[start][1])

def inOrder(start):
    if start != -18:
        inOrder(tree[start][0])
        print(chr(start+64), end="")
        inOrder(tree[start][1])

def postOrder(start):
    if start != -18:
        postOrder(tree[start][0])
        postOrder(tree[start][1])
        print(chr(start+64), end="")

n = int(input())
tree = [[] for _ in range(n+1)]

# 아스키 코드로 넣어주기
for i in range(n):
    a, b, c = input().split()
    a, b, c = ord(a)-64, ord(b)-64, ord(c)-64

    tree[a].append(b)
    tree[a].append(c)

# 전위 중위 후위
preOrder(1)
print()
inOrder(1)
print()
postOrder(1)
