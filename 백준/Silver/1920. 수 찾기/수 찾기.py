import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
A.sort()

for num in B:
    l, r = 0, N-1
    isExist = False
    #이분 탐색
    while l <= r:
        mid = (l + r) // 2
        if A[mid] == num:
            isExist = True
            print(1)
            break
        elif A[mid] < num:
            l = mid + 1
        else:
            r = mid - 1
    if not isExist:
         print(0)