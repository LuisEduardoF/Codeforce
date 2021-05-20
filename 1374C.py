def count_brackets(string):
	left = 0
	for let in string:
		if(let == '('):
			left += 1
		else:
			if(left > 0):
				left -= 1
	print(left)
	
n = int(input())
for i in range(n):
	s = int(input())
	string = input()
	count_brackets(string)






	