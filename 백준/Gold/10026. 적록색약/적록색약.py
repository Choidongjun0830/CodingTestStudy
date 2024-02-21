import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())

painting = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, color):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx <= N-1 and 0 <= ny <= N-1 and visited[nx][ny] == 0 and painting[nx][ny] == color:
                dfs(nx,ny, visited, color)


#적록색약 X
X_visited = [[0] * N for i in range(N)]
X_count = 0
for i in range(N):
    for j in range(N):
        if not X_visited[i][j]:
            color = painting[i][j] 
            dfs(i,j, X_visited, color)
            X_count +=1

#적록색약 O
#초록색을 빨간색으로 변경
for i in range(N):
    for j in range(N):
        if painting[i][j] == 'G':
            painting[i][j] = 'R'
O_visited = [[0] * N for i in range(N)]
O_count = 0
for i in range(N):
    for j in range(N):
        if not O_visited[i][j]:
            color = painting[i][j] 
            dfs(i,j, O_visited, color)
            O_count +=1

print(X_count,O_count)
