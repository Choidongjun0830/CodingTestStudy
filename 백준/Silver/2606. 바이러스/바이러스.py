import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
V = int(input())

graph = [[] for i in range(N+1)]
for i in range(V):
    a ,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)

def bfs(V):
    count = 0
    queue = deque()
    queue.append(V)
    visited[V] = 1
    while queue:
        
        node = queue.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                queue.append(n)
                visited[n] = 1
                count += 1
    return count

print(bfs(1))
