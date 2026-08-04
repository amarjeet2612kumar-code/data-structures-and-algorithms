"""
Zigzag
  *     *   
 * *   * *  
*   * *   * 
"""


def zigZag(n):
  for row in range(3):
    for col in range(n):
      if row == 0 and col%4==2:
        print("*",end="")
      elif row == 1 and col % 2 == 1:
        print("*",end="")
      elif row  == 2 and col % 4 ==0:
        print("*",end="")
      else:
        print(" ",end="")
    print("")



zigZag(13)