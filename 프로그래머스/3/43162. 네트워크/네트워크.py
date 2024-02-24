from collections import deque

def solution(n, computers):
        
    def bfs(V):
        queue = deque([V])
        visited[V] = True
        while queue:
            com = queue.popleft()
            for i in range(n):
                if computers[com][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
    return answer