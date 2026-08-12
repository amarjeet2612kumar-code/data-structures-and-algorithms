"""
Sum of Digits 
Input: 58392
output=27
"""

def sumOfDigits(n):
	sum=0
	while n>0:
		sum=sum + n % 10
		n=n//10
	print("Sum of Digits",sum)

n=123456
sumOfDigits(n)