Let us consider the following problem to understand Binary Indexed Tree.
We have an array arr[0 . . . n-1]. We would like to 
1 Compute the sum of the first i elements. 
2 Modify the value of a specified element of the array arr[i] = x where 0 <= i <= n-1.

Both operations time complexity).

pros:  answers each query in O(logn) , preprocessing done in  O(nlogn) 
Cons: Fenwick tree can only be used for queries with l=0(0<=r<n), so it is not applicable to many problems.
