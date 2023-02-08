import sys
def input(): return sys.stdin.readline().rstrip()

from math import gcd
from random import randrange

def modular_pow(base, exponent, modulus):
	result = 1
	while (exponent > 0):
		if (exponent & 1):
			result = (result * base) % modulus
		exponent = exponent >> 1
		base = (base * base) % modulus
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
		
	potential_witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
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

		if (d == n):
			return PollardRho(n)
	if isPrime(d):
		return d
	return PollardRho(d)

n = int(input())
factors=[]
n_copy = n

while n > 1:
	k = PollardRho(n)
	factors.append(k)
	n //= k
factors = sorted(set(factors))

for i in factors:
	n_copy *= i - 1
	n_copy //= i

print(int(n_copy))