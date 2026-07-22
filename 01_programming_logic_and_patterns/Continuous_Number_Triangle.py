"""
Continuous Number Triangle
1
23
456
78910
1112131415
"""

def continuousNumberTriangle(n):
	counter=1
	for row in range(n):
		for col in range(row+1):
			print(counter,end="")
			counter+=1
		print()

continuousNumberTriangle(5)