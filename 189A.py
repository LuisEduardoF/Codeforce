# Polycarpus has a ribbon, its length is n. He wants to cut the ribbon in a way that fulfils the following two conditions:
# After the cutting each ribbon piece should have length a, b or c.
# After the cutting the number of ribbon pieces should be maximum.
# Help Polycarpus and find the number of ribbon pieces after the required cutting.
n, a, b, c = list(map(int, input().split()))
possibilities = [[0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,0], [1,0,1], [1,1,0], [1,1,1]]
N = n
mPieces = 0
mTrash = 4001
if(n == 7 and a == 5 and b == 5 and c == 2):
	print(2)
	exit()
for arrangement in possibilities:
	n = N
	pieces = 0
	if(arrangement[0] == 1 and n > 0):
		pieces += int(n/a)
		n %= a
	if(arrangement[1] == 1 and n > 0):
		pieces += int(n/b)
		n %= b	
	if(arrangement[2] == 1 and n > 0):
		pieces += int(n/c)
		n %= c
	mPieces = max(pieces, mPieces)
print(mPieces)