"""
Digital Root 
The digital root means repeatedly adding the digits of a number until only one digit remains.
Input:  12345

1 + 2 + 3 + 4 + 5 = 15

1 + 5 = 6
"""

def digitalRoot(n):

	root_sum=0
	while n > 0 :
		root_sum = root_sum + (n%10)
		n=n//10
		#if (n == 0 and (root_sum//10)!=0):
		if (n == 0 and root_sum>9):
			n = root_sum
			root_sum=0

	print("Root Sum",root_sum)


n=12345
digitalRoot(n)