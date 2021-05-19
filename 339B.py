#Xenia lives in a city that has n houses built along the main ringroad. The ringroad houses are numbered 1 through n in the clockwise order. The ringroad traffic is one way and also is clockwise.
#Xenia has recently moved into the ringroad house number 1. As a result, she's got m things to do. In order to complete the i-th task, she needs to be in the house number ai and complete all tasks with numbers less than i. Initially, Xenia is in the house number 1, find the minimum time she needs to complete all her tasks if moving from a house to a neighboring one along the ringroad takes one unit of time.
n, m = list(map(int, input().split()))
board = list(map(int, input().split()))
ant = board[0]
pos = 0
pos += board[0] - 1
for i in range(len(board)-1):
	if(board[i+1] > ant):
		pos += board[i+1] - ant
	elif(board[i+1] < ant):
		pos += ( n - ant ) + board[i+1]
	ant = board[i+1]
print(pos)
