"""
Increasing Number Triangle 
1
12
123
1234
12345
"""
def increasingNumberTriangle(n):
	for row in range(1,n+1):
		for col in range(1,row+1):
			print(col,end="")
		print()


increasingNumberTriangle(5)