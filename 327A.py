def find_0subsequence(board):
	mSubsequence = 0
	subsequence = 0
	nOne = 0
	for i in range(len(board)):
		if(board[i] == 0):
			subsequence += 1
		else:
			mSubsequence = max(subsequence, mSubsequence)
			subsequence = 0
			nOne += 1
	mSubsequence = max(subsequence, mSubsequence)
	if(mSubsequence > 0):
		return mSubsequence + nOne
	else:
		return nOne - 1
n = int(input())
board = list(map(int, input().split()))
print(find_0subsequence(board))