from math import log

import copy


# logic vector

def lvec(bits = 8, n = 0):
	"""
		returns a logic vector for x_n
	"""
	vre = [0 for _ in range(bits)]

	index = 0

	n = 2**n

	x = 0

	while index < bits:
		for _ in range(n):
			vre[index] = x
			index += 1
		x = 1 if x == 0 else 0
	
	return vre


def lvecs(n):
	"""
		returns all logic combination of n bit input
			A, B, C, .... = lvecs(n) * n is number of inputs

			e.g.
				A, B, C, D, E = lvecs(5)
	"""
	return tuple(lvec(2**n, n-i-1) for i in range(n))


def vec(x, bits):
	"""
		returns vector representation of an output signal when given  as a number

		**input 0x before a number so that python interpret it as a hexadecimal number

			e.g. 0xA5 = 165
	"""

	v = list()

	for _ in range(bits):
		v.append(x%2)
		x //= 2

	return v[::-1]



# logic vector ooperation


def nicht(v):
	"""
		negates a logic vector
	"""

	return [1 if x == 0 else 0 for x in v]


def und(A, B):
	"""
		and operation on two logic vectors
	"""

	return [a and b for a, b in zip(A, B)]


def oder(A, B):
	"""
		or operation on two logic vectors
	"""

	return [a or b for a, b in zip(A, B)]


def xor(A, B):
	"""
		xor operation on two logic vectors
	"""

	return [ 0 if a == b else 1 for a, b in zip(A, B)]


def kmapv(n = 3):
	"""
		returns the first row of the karnaugh matrix
	"""
	if n < 1:
		return [0]

	v0 = kmapv(n-1)

	if n%2 == 0:
		return [2*x for x in v0]

	m = 2**(n-1)

	n = (n+1)//2

	n = 2**n

	v = list(0 for _ in range(n))

	for i in range(n//2):
		v[i] = v0[i]//2
		v[n -1 -i] = v[i] + m

	return v


def kmapm(n = 3):
	"""
		Generate a Karnaugh matrix filled with the decimal representation of the input ABCD...
	"""
	v = kmapv(n)

	if n%2 == 0:
		n = 2**(n//2)
		m = n
		u = [x//2 for x in v]
	else:
		n = 2**((n+1)//2)
		m = n//2
		u = [2*x for x in v[:len(v)//2]]

	mre = [[0 for _ in range(n)] for _ in range(m)]

	for i in range(m):
		for j in range(n):
			mre[i][j] = v[j] + u[i]
	
	return mre


def kmap(v, m = None, n = None):
	"""
		Generate a matrix mapping the output vector v to the Karnaugh map of the inputs
	"""
	if m is None:
		if n is None:
			n = int(log(len(v), 2))		# Everything is gonna be fine over here
		m = kmapm(n)
	else:
		m = copy.deepcopy(m)

	for i, row in enumerate(m):
		for j, _ in enumerate(row):
			row[j] = v[row[j]]
	
	return m


def show(m, sep = ' ', nline = '\n', verbose = True):
	"""
		print a matrix

		return a str of what being printed
			* set verbose to False to suppress screen print
	"""

	S = nline.join(sep.join(str(x) for x in row) for row in m)

	if verbose:
		print(S)

	return S


def show_v(v, sep = ' ', verbose = False):
	"""
		return a str of the logic vector

		print a the vector
			* set verbose to True to print
	"""

	S = sep.join(str(x) for x in v)

	if verbose:
		print(S)

	return S


def show_sector(n_bit = 4, i = None, m = None):
	"""
		shows how the Karnaugh map would look when the output match the input
			- bits is the number of the input signals
			- i can be a specif input
				- if i is not provided, all possible combinations will be shown
	"""

	def show_n(m, n, i):	# local fucntion
		v = lvec(2**n, i)
		km = kmap(v, m)
		print(f"\n\n{chr(65+n-i-1)}:\n")
		show(km)

	if m is None:
		m = kmapm(n_bit)

	print("\n\nKarnaugh-Diagram mapping the output to input\n\n")

	if i is not None:
		show_n(m, n_bit, i)
		return
	
	for i in range(n_bit-1, -1, -1):
		show_n(m, n_bit, i)



def demo1():
	"""
		This is ment to be an example how to use this code
	"""

	# Anzahl der Eingänge
	n = 3

	# Eingang Signals
	S, X0, X1 = lvecs(3)

	print(
	"""
\n
    In this demo

    A is representing S
    B is representing X1
    C is representing X0
\n
	"""
	)

	print(f"X1:\t{show_v(X1)}")
	print(f"X0:\t{show_v(X0)}")
	print(f"S:\t{show_v(S)}")

	print('\n')

	# f = ((not S) and X0) or (S and X1)		;)

	f = oder(

		und(
			nicht(S), X0
			),

		und(
			S, X1
		)
	)

	# Karnaugh map mit Dezimalzahlen
	m = kmapm(n)

	# Karnaugh-Diagram der Ausgangssignal
	km = kmap(f, m)

	show(km)


def demo0(n = 3):
	show_sector(n)


def main():

	demo0()

	demo1()

	print('\n\n')



def demo5():
	show_sector(5)

def demo6():
	show_sector(6)


if __name__ == "__main__":

	main()


	# run more demos

	# demo5()
	# demo6()

	# show_sector(# as high as you want #) 


