"""
Count Digits 
Input:  58392
Output: 5
"""

def countDigits(n):
	counter=0
	while n>0:
		n=n//10
		counter+=1
	print("Lenght of Digits:-",counter)


n=85445
countDigits(n)