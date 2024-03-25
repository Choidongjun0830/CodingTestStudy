import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())

tree = [[]for i in range(n+1)]
for i in range(n-1):
  input = list(map(int,sys.stdin.readline().split()))
  tree[input[0]].append((input[1],input[2]))
  

def dfs(start):
  global result
  left, right = 0, 0 
  for node,d in tree[start]:
    distance = dfs(node) + d # distance = left + d.
    if distance > left:
      left,right = distance, left #계속해서 비교해나가기 위해 더 긴 것을 left, 더 짧은 것을 right
    elif distance > right:
      right = distance
    result = max(result, left + right)

  return left #더 긴 길이는 left이기 때문에 left이기 때문에 distance = dfs(node) + d에 left가 이용되어야 한다.
  
distance = 0  
result = 0
dfs(1)
print(result)