from collections import deque,defaultdict
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
g = defaultdict(list)
noe = len(edges)
for i in range(noe):
  u = edges[i][0]
  v = edges[i][1]
  g[u].append(v)
  g[v].append(u) 
bfs(n,g)                     
