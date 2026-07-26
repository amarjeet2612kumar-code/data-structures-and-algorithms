"""
Continuous Alphabet Triangle
A
BC
DEF
GHIJ
KLMNO
"""

def continuousAlphabetTriangle(n):
	alpha=65
	for row in range(n):
		for col in range(row+1):
			print(chr(alpha),end="")
			alpha+=1
		print()


continuousAlphabetTriangle(5)
