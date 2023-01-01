https://www.geeksforgeeks.org/modulo-1097-1000000007/
https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/

To find (x/y)%m 
y_inv = mmi(y,m)
ans = (x*y_inv)%m

Modular multiplicative inverse when M is prime:
Time Complexity: O(log M)
Auxiliary Space: O(log M), because of the internal recursion stack.
