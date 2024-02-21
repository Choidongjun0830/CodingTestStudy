import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
T = int(input())
    
def dfs(x, y):
    #방문처리
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= M-1 and graph[nx][ny] == 1:
            dfs(nx,ny)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for test in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * M for i in range(N)]
    for i in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i,j)
                count += 1
    print(count)
