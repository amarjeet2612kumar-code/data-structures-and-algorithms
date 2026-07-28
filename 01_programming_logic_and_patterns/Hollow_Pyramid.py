"""
Hollow Pyramid 
    *
   * *
  *   *
 *     *
*********
"""

def hollowPyramid(n):
    if n <= 0:
        return
        
    for row in range(1, n + 1):
        # 1. Top Vertex (First Row)
        if row == 1:
            print(" " * (n - 1) + "*")
            
        # 2. Bottom Base (Last Row)
        elif row == n:
            print("*" * (2 * n - 1))
            
        # 3. Middle Hollow Rows
        else:
            outer_spaces = " " * (n - row)
            inner_spaces = " " * (2 * row - 3)
            print(outer_spaces + "*" + inner_spaces + "*")



def hollowPyramidNested(n):
    for row in range(n):
        for col in range(2 * n - 1):
            # Condition 1: Left slope boundary
            if col == (n - 1 - row): 
                print("*", end="")
            # Condition 2: Right slope boundary
            elif col == (n - 1 + row) :
                print("*", end="")
            # Condition 3: Bottom solid base
            elif row == n - 1:
                print("*", end="")
            # Condition 4: printing space inside the pyramid
            else:
                print(" ", end="")
        print() 



hollowPyramid(5)

hollowPyramidNested(5)