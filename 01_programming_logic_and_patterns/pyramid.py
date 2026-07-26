"""
Problem:
Print pyramid / diamond pattern
    *
   ***
  *****
 *******
*********

Expected Output:

"""

def pyramid(n):
    for j in range(n):
        print(" "*(n-j-1),"*"*(2*j -1 + 2))
            
pyramid(5)