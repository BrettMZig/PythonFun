

def composite_gen(prime, first, last):
	c = prime + prime
	while c < last:
		if c > first: 
			yield c
		c = c + prime
	


def find_primes(first, last):
	if first < 2: first = 2
	
	mSet = set(xrange(first, last))
	primes = []
	
	for x in xrange(2, last):
		if x in mSet:
			primes.append(x)		
		mSet = mSet - set(composite_gen(x, first, last))
	
	return primes



if __name__ == "__main__":
	first = 200
	last = 10000
	print find_primes(first, last)
	
