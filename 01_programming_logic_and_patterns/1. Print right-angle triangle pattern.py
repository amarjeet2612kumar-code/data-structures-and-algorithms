"""
Problem:
Print a right-angle triangle.

Expected Output:
*
**
***
****
*****

Observation:
- Total rows = n
- Number of stars equals the row number.

Algorithm:
1. Iterate through each row.
2. Print stars according to the current row.
3. Move to the next line.
"""

def print_right_angle_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

# Example usage:
print_right_angle_triangle(5)