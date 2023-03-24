import sys
input = lambda: sys.stdin.readline().rstrip()
from math import gcd
from random import randrange

MOD = 1000000007

def modular_pow(base, exponent, modulus):
	result = 1
	while (exponent > 0):
		if (exponent & 1):
			result = (result * base) % modulus
		exponent = exponent >> 1
		base = (base * base) % modulus
	return result

def modular_pow_womod(base, exponent):
	result = 1
	while (exponent > 0):
		if (exponent & 1):
			result = (result * base) % (MOD ** 5)
		exponent = exponent >> 1
		base = (base * base) % (MOD ** 5)
	return result

def miller_rabin(n, a):
	d = n - 1
	while d % 2 == 0:
		if modular_pow(a, d, n) == n - 1:
			return True
		d //= 2
	t = modular_pow(a, d, n);
	return t == n - 1 or t == 1

def isPrime(n):
	if n == 1 or n % 2 == 0:
		return False
		
	potential_witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23]    # n <= 2e18
	for a in potential_witnesses:
		if n == a:
			return True
		if not miller_rabin(n, a):
			return False
	return True

def PollardRho(n):
	if isPrime(n):
		return n
		
	if n == 1:
		return 1
	if n % 2 == 0:
		return 2

	x = randrange(2, n)
	y = x
	c = randrange(1, n)
	d = 1

	while d == 1:
		x = (modular_pow(x, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		y = (modular_pow(y, 2, n) + c + n)%n
		d = gcd(abs(x - y), n)

		if d == n:
			return PollardRho(n)
	if isPrime(d):
		return d
	return PollardRho(d)


n, x, y, m = map(int,input().split())
X, Y = abs(x), abs(y)

###
# Prime factorize |x+y|, |x|, |y| with Pollard Rho
Pxy = []
PX = []
PY = []
for P, v in [Pxy, abs(x + y)], [PX, X], [PY, Y]:
    if v == 1:
        P.append(0)
    while v > 1:
    	k = PollardRho(v)
    	P.append(k)
    	v //= k
#print("P(|x+y|) =", *Pxy) #
#print("P(|X|) =", *PX) #
#print("P(|Y|) =", *PY) #

# Discard factors that divides X or Y
P = list(set(Pxy).difference(PX, PY))
#print("P:", *P) #

if P == [0]:
    print(1,1)
    exit(0)

###
# LTE lemma
f = []
for pi in P:
    vpiXY = 0
    t = x + y
    while t % pi == 0:
        vpiXY += 1
        t //= pi

    vpin = 0
    t = n
    while t % pi == 0:
        vpin += 1
        t //= pi
        
    f.append(vpiXY + vpin)
#print("f:", *f) #

###
# Calculating len(dm), sum(dm)
g = []
for fi in f:
    g.append(fi//m)
#print("g:", *g) #

len_dm = 1
for gi in g:
    len_dm *= 1+gi
    len_dm %= MOD

sum_dm = 1
for gi, pi in zip(g, P):
    sum_dm *= (modular_pow_womod(pi, (gi+1)*m) - 1) // (modular_pow_womod(pi, m) - 1)
    sum_dm %= MOD

print(len_dm, sum_dm)