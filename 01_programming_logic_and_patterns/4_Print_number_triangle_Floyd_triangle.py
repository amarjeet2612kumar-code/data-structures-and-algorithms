"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

Observation :-
row = 5
column = 5
Every row increase by one number which increase by 1 of previous number
"""

def floyd_tringle(n):
	counter = 1
	for row in range(1,n+1):
		for col in range(row):
			print(counter,end=" ")
			counter+=1
		print("")
	

floyd_tringle(5)