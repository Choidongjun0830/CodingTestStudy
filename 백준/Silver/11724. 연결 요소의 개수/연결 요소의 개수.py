import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())


graph = [[] for i in range(N+1)]
for i in range(M):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dfs_visited = [0] * (N+1)
def dfs(V):
    dfs_visited[V] = 1
    for v in graph[V]:
        if not dfs_visited[v]:
            dfs(v)

dfs_count = 0
for i in range(1, N+1):
    if not dfs_visited[i]:
        dfs(i)
        dfs_count += 1

print(dfs_count)