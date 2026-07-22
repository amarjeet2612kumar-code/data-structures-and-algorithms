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
        print(" "*int(n-j-1),"*"*int(2*j -1 + 2))
            

pyramid(5)