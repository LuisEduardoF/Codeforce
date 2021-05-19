# Olesya loves numbers consisting of n digits, and Rodion only likes numbers that are divisible by t. Find some number that satisfies both of them.

# Your task is: given the n and t print an integer strictly larger than zero consisting of n digits that is divisible by t. If such number doesn't exist, print  - 1.
import math
n, t = list(map(int, input().split()))
log = int(math.log(t, 10))
if( log >= n ):
	print(-1)
else:
	print((10**(n - log - 1))*t)

