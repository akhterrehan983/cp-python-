  from sortedcontainers import SortedList, SortedSet, SortedDict

  sorted_list = SortedList([1, 2, 10, 4])
  sorted_list.add(-1)
  sorted_list.discard(2)
  sorted_list.update([3,20])
  print(sorted_list)
  sorted_list.clear()
  print(sorted_list)
