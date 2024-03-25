import sys
import copy
from itertools import combinations
from collections import deque
sys.setrecursionlimit(10 ** 8)

# 0 : 빈칸, 1 : 벽, 2 : 바이러스
#바이러스는 상하좌우로 인접한 빈칸. 새로 세울 수 있는 벽의 개수는 3개
N, M = map(int, sys.stdin.readline().split())

#전체 graph, 0의 인덱스들, 바이러스가 있는 인덱스들
graph = []
zeros = []
viruses = []
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)
    for j, x in enumerate(row):
        if x == 0:
            zeros.append((i,j))
        elif x == 2:
            viruses.append((i,j))
#zeros에 있는 인덱스들 3개씩 조합 만들기
zeros_combi = list(combinations(zeros, 3))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
temp = []
for c in zeros_combi:
    temp = copy.deepcopy(graph)
    cnt = 0
    for wall in c: #벽 세우기
        temp[wall[0]][wall[1]] = 1
    queue = deque(viruses)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                queue.append((nx,ny))
    for row in temp:
        for val in row:
            if val == 0:
                cnt += 1
    result = max(result, cnt)

print(result)
