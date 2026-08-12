"""
Product of Digits 
Input:  1234
Output: 24
"""

def productOfDigits(n):
	prod_of_digits=1
	while n>0:
		prod_of_digits=prod_of_digits * (n%10)
		n=n//10
	print("Product of Digits:-",prod_of_digits)

n=1234
productOfDigits(n)

