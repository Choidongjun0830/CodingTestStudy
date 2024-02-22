from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def bfs(X, Y):
        queue = deque()
        queue.append((X,Y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
                    
        return maps[n-1][m-1]
    
    result = bfs(0,0)
    if result == 1:
        return -1
    else:
        return result