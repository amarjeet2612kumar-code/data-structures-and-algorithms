"""
Problem:
Print inverted triangle pattern

Expected Output:
*****
****
***
**
*
"""

def print_right_angle_triangle(n):
	while n>=1:
		print("*"*n)
		n-=1

print_right_angle_triangle(5)



def print_right_angle_triangle_2(n):
	for i in range(n,0,-1):
		print("*"*i)

print_right_angle_triangle_2(5)