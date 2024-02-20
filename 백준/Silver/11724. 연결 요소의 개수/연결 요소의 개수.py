import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())


graph = [[] for i in range(N+1)]
for i in range(M):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
bfs_visited = [0] * (N+1)
def bfs(V):
    queue = deque()
    queue.append(V)
    bfs_visited[V] = 1
    while queue:
        startNode = queue.popleft()
        for v in graph[startNode]:
            if not bfs_visited[v]:
                queue.append(v)
                bfs_visited[v] = 1
bfs_count = 0
for i in range(1, N+1):
    if not bfs_visited[i]:
        bfs(i)
        bfs_count += 1

print(bfs_count)