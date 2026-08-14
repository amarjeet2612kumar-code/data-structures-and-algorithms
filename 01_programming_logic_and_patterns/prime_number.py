"""
Prime Number
7
↓
check divisibility
↓
only 1 and 7 divide it
↓
2 divisors
↓
Prime

1, 2, 3, 4, 6, 12
        ↓
    more than 2
        ↓
    Not Prime
"""

def primeNumber(n):
	count=0
	for i in range(1,n+1):
		if n%i == 0 :
			count+=1

	if count == 2:
		print("prime Number",n)
	else:
		print("not prime Number",n)

#n=7
#primeNumber(n)

#n=12
#primeNumber(n)


"""
n=36
1 × 36
2 × 18
3 × 12
4 × 9
6 × 6
"""

def optimizedPrimeNumber(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
        	print("not prime Number", n)    
        	return        
        i += 1  
    print("prime Number", n)

n=36
optimizedPrimeNumber(n)
n=37
optimizedPrimeNumber(n)