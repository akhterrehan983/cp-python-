Time Complexity: O(n+k)
Auxiliary Space: O(k)

(Modular Inversion technique) for nCk

1. The general formula of nCr is ( n*(n-1)*(n-2)* … *(n-r+1) ) / (r!). 
We can directly use this formula to find nCr. But that will overflow out of bound. 
We need to find nCr mod m so that it doesn’t overflow. We can easily do it with modular arithmetic formula. 

for the  n*(n-1)*(n-2)* ... *(n-r+1) part we can use the formula,
(a*b) mod m = ((a % m) * (b % m)) % m

2. and for the 1/r! part, we need to find the modular inverse of every number from 1 to r. Then use the same formula above with a modular inverse of 1 to r. We can find modular inverse in O(r) time using  the formula, 

inv[1] = 1
inv[i] = − ⌊m/i⌋ * inv[m mod i] mod m
To use this formula, m has to be a prime.
