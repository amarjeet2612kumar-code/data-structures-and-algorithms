"""
Butterfly
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""

def butterFly(n):
	for row in range(n):
		left=row+1
		space=2*(n-row-1)
		right=row+1
		print("*"*left+" "*space+'*'*right)
	for row in range(n,0,-1):
		left=row-1
		space=2*(n-row+1)
		right=row-1
		print("*"*left+" "*space+'*'*right)


butterFly(5)
