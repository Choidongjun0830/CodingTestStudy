import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    clothes = {}
    N = int(input())
    for j in range(N):
        name, category = input().split()
        if category not in clothes:
            clothes[category] = [name]
        else:
            clothes[category].append(name)
    result = 1
    for cate in clothes:
        length = len(clothes[cate])
        result *= length + 1
    print(result - 1)