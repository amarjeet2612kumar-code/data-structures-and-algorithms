"""
Diamond 

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""

def diamond(n):
    for i in range(n-1):
        space = n-i-1
        star = 2*i+1
        print(" "*space,"*"*star)
    for j in range(n):
        space = 2*j-j 
        star = 2*n-2*j-1
        print(" "*space,"*"*star)

diamond(5)