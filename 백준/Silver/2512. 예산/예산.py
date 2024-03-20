import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))
M = int(input())

if sum(li) <= M:
    print(max(li))
else:
    result = 0
    start = 0
    end = max(li)
    while start <= end:
        mid = (start + end) // 2
        sums = 0
        for l in li:
            if l < mid:
                sums += l
            else:
                sums += mid
        if sums <= M:
            start = mid + 1
        else:
            end = mid - 1
    print(end)