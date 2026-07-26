"""
Same Alphabet Triangle 
A
BB
CCC
DDDD
EEEEE
"""

def sameAlphabetTriangle(n):
	alpha=65
	for row in range(n):
		for col in range(row+1):
			print(chr(alpha),end="")
		alpha+=1
		print()
		


sameAlphabetTriangle(5)