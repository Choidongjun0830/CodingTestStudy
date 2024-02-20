import sys
from collections import deque

N, M, V = map(int,sys.stdin.readline().split())

#graph 입력 받기
graph = [[0]* (N+1) for i in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

dfs_visited = [0] * (N+1)
def dfs(start_Node):
    dfs_visited[start_Node] = 1
    print(start_Node, end = ' ')
    for i in range(1, N+1):
        if dfs_visited[i] == 0 and graph[start_Node][i] == 1:
            dfs(i)

bfs_visited = [0] * (N+1)
def bfs(start_Node):
    queue = deque()
    queue.append(start_Node)
    bfs_visited[start_Node] = 1
    while queue:
        start_Node = queue.popleft()
        print(start_Node, end= ' ')
        for i in range(1, N+1):
            if bfs_visited[i] == 0 and graph[start_Node][i] == 1:
                queue.append(i)
                bfs_visited[i] = 1

dfs(V)
print()
bfs(V)
