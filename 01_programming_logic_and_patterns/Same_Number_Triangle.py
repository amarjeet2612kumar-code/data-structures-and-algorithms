"""
1
22
333
4444
55555
"""

def sameNumberTringle(n):
	for i in range(1,n+1):
		print(f"{i}"*i)

def sameNumberTringle2(n):
	for row in range(1,n+1):
		for col	in range(1,row+1):
			print(row,end="")
		print()

sameNumberTringle(5)

sameNumberTringle2(5)