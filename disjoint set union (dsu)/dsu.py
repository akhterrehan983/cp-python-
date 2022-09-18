from collections import defaultdict
class DisjSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def Union(self, x, y):
        
        # Find current sets of x and y
        xset = self.find(x)
        yset = self.find(y)

        # If they are already in same set
        if xset == yset:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset

        elif self.rank[xset] > self.rank[yset]:
            self.parent[yset] = xset

        # If ranks are same, then move y under
        # x (doesn't matter which one goes where)
        # and increment rank of x's tree
        else:
            self.parent[yset] = xset
            self.rank[xset] = self.rank[xset] + 1

# Driver code
n = int(input()) #nodes
noe = int(input()) #edges
obj = DisjSet(n+1)
for i in range(noe):
  x,y = map(int,input().split())
  obj.Union(x,y)

  # for no of connected components
from collections import defaultdict
dict_pair = defaultdict(list)
for idx, val in enumerate(obj.parent):
  dict_pair[obj.find(val)].append(idx)
print(len(dict_pair.keys()))
