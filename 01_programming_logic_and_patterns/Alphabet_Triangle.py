"""
Alphabet Triangle 
A
AB
ABC
ABCD
ABCDE
"""

def alphabetTriangle(n):
	for row in range(n+1):
		alpha=65
		for col in range(row):
			print(chr(alpha),end="")
			alpha+=1
		print("")



alphabetTriangle(5)