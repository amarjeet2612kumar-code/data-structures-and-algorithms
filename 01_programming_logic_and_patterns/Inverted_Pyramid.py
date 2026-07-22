"""
Inverted Pyramid
*********
 *******
  *****
   ***
    *
"""


def inverted_pyramid(n):
	for i in range(n):
		star=2*n - 2*i - 1
		space= 2 * i - i
		print(" "*space,"*"*star)

inverted_pyramid(5)