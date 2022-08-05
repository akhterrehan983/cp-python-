import heapq

# initializing list
li = [5, 7, 9, 1, 3]
heapq.heapify(li)

print ("The created heap is : ",end="")
print (list(li))

heapq.heappush(li,4)
print ("The popped and smallest element is : ",end="")
print (heapq.heappop(li))

#It is by default a min heap. To make this max heap just use negative(-) sign before the element while pushing and after popping.
