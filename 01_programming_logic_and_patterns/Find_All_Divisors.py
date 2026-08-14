"""
Find All Divisors
Input: 12
Output: 1 2 3 4 6 12
12 ÷ 1 = 12
12 ÷ 2 = 6
12 ÷ 3 = 4
12 ÷ 4 = 3
12 ÷ 6 = 2
12 ÷ 12 = 1
"""

def findAllDivisors(n):
	for i in range(1,n+1):
		if (n%i) == 0 :
			print(n,"÷",i,"=",n//i)

n=12
findAllDivisors(n)