import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
V = int(input())

graph = [[] for i in range(N+1)]
for i in range(V):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
count = 0
def dfs(V):
    global count
    visited[V] = 1
    for n in graph[V]:
        if visited[n] == 0:
            dfs(n)
            count += 1

dfs(1)
print(count)
