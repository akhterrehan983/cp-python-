from collections import deque
def bfs(n,g):
  vis = [False]*n
  for i in range(n):
        if not(vis[i]):
            q = deque()
            q.append(i)
            vis[i] = True
            while(q):
                node = q.popleft()
                print(node)
                for e in g[node]:
                    if not(vis[e]):
                      q.append(e)
                      vis[e] = True
bfs(n,g)                     
