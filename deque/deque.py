from collections import deque
  
# de = deque([])
de = deque([1,2,3])
print(de)

de.append(4)
de.appendleft(6)
print(de)

de.pop()
print (de)
de.popleft()
print (de)
