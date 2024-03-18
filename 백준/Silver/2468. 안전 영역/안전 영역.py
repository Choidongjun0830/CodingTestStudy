import sys
sys.setrecursionlimit(10 ** 8)

N = int(sys.stdin.readline())
matrix = []
for i in range(N):
    matrix.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y, depth):
    #방문하면 0으로
    visited[x][y] = 1
    #depth보다 높으면서, 방문하지 않은곳
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <= N-1 and 0 <= ny <= N-1:
            if visited[nx][ny] != 1 and matrix[nx][ny] > depth:
                dfs(nx, ny, depth)

results = []
depth = 0
while True:
    # visited는 depth를 실행할 때마다 초기화해줘야함.
    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > depth and visited[i][j] != 1:
                dfs(i, j, depth)
                count += 1
    if count == 0:
        break
    results.append(count)
    depth += 1
print(max(results))