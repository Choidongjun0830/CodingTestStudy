import sys
sys.setrecursionlimit(10**6)
    
def dfs(V, color):
    colors[V] = color
    for node in graph[V]:
        if colors[node] == 0: #colors는 0, -1, 1
            result = dfs(node, -1 * color)
            if not result:
                return False
        elif colors[V] == colors[node]:
            return False
    return True
        


input = sys.stdin.readline
K = int(input())

for i in range(K):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)]
    for i in range(E):
        u, v= map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    colors = [0] * (V+1)
    for i in range(1, V+1):
        if not colors[i]:
            result = dfs(i,1)
        if not result:
            break
    print("YES" if result else "NO")