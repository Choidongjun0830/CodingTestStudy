import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            return dist[x]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= 10 ** 5 and not dist[nx]:
                dist[nx] = dist[x] + 1
                queue.append(nx)

dist = [0] * (10**5 + 1)
print(bfs())
