PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)

def sieve_of_eratosthenes(bis):
	N = list(range(3, bis+1 if bis%2 else bis, 2))
	
	p, index = 3, 0

	index_of = lambda n: (n-3)//2
	
	while not (index := p*p) > bis:
		step = 2*p
		while not index > bis:
			N[index_of(index)] = 0
			index += step
		
		while (N[index_of(p := p + 2)]) == 0:
			pass
	
	return ( 2, *(x for x in N if x != 0) )


def nonzero(A):
	return *(a for a in A if a != 0),


def extend_sieve_of_eratosthenes(bis, P):
	
	von = P[-1] + 2

	N = list(range(von, bis+1 if bis%2 else bis, 2))

	index_of = lambda n: (n-von)//2



	foothold = lambda p: (r + 1 + r%2)*p if von - p*(r := von//p) else r*p

	index = 0

	for p in P[1:]:
		if p*p > bis:
			break
		step = 2*p
		index = foothold(p)
		while not index > bis:
			N[index_of(index)] = 0
			index += step

	if not (von*von) > bis:
		p = P[-1]

		# NOT Wasserdict
		# Unlikly to break, but still
		while (N[index_of(p := p + 2)]) == 0:
			pass
		
		while not (index := p*p) > bis:
			step = 2*p
			while not index > bis:
				N[index_of(index)] = 0
				index += step
			
			while (N[index_of(p := p + 2)]) == 0:
				pass
		
	return ( *P, *(x for x in N if x != 0) )


# Alias for the main methode to find Prime
def primes(bis = 10**3):
	return sieve_of_eratosthenes(bis)

def extend_primes(bis = 10**3, P = PRIMES):
	return extend_sieve_of_eratosthenes(bis, P)




# Euclidean algorithm
# greatest common divisor
def gcd (x, y):
	if x == y:
		return x
	x, y = (x, y) if x > y else (y, x)
	return gcd(x-y, y)

