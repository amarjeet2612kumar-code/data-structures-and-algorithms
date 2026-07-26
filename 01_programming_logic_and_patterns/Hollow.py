"""
Hollow Rectangle 
Option 1: Square (Most Common in DSA)
n = 5
*****
*   *
*   *
*   *
*****

Option 2: Rectangle (More Flexible)
rows = 5
cols = 7
*******
*     *
*     *
*     *
*******

Option 3: One n, Derive the Other
rows = n
cols = 2*n
For n = 4:
********
*      *
*      *
********
"""

def hollowSquare(n):
	print("------Square------")
	for row in range(n):
		for col in range(n):
			if row == 0 or row == n - 1 or col == 0 or col == n - 1:
				print("*", end="")
			else:
				print(" ", end="")
		print()


def hollowRectangle(rows,cols):
	print(f"------Rectangle Shape {rows,cols}------")
	for row in range(rows):
		for col in range (cols):
			if row == 0 or row==rows-1 or col == 0 or col == cols-1:
				print("*", end="")
			else:
				print(" ", end="")
		print()


def hollowDerive(n):
	print("------Derive Shape------")
	cols = 2*n
	rows = n
	for row in range(rows):
		for col in range (cols):
			if row == 0 or row==rows-1 or col == 0 or col == cols-1:
				print("*", end="")
			else:
				print(" ", end="")
		print()



hollowSquare(5)

hollowRectangle(5,7)

hollowRectangle(7,5)


hollowDerive(8)