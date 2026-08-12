"""
Palindrome Number 
it's a palindrome.
123
 ↓
321
it's not a palindrome
123 != 321
"""


def palindrome(n):
	rev=0
	original=n
	while n > 0:
		rev = (rev*10)+n % 10
		n=n//10

	if rev != original:
		print("Given no is not palindrome",rev)
	else:
		print("Given no is palindrome",rev)


n=123
palindrome(n)

n=121
palindrome(n)