import sys
def input(): return sys.stdin.readline().rstrip()

from math import gcd, sqrt
from random import randrange
from collections import Counter

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
		
	fermat_witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23]
	for a in fermat_witnesses:
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

def factorize(n):
	factors = []
	while n > 1:
		k = PollardRho(n)
		factors.append(k)
		n //= k
	return sorted(factors)


def sum_of_four_squares(n):
	while n % 4 == 0:
		n //= 4
	return n % 8 == 7

def sum_of_three_squares(n):
	for i, cnt in Counter(factorize(n)).items():
		if i % 4 == 3 and cnt % 2 == 1:
			return True
	return False

def sum_of_two_squares(n):
	if n == 1:
		return False
	return not is_square(n)
	
def is_square(n):
	x = n // 2
	seen = {x}
	while x * x != n:
		prev = x
		x = (x + (n // x)) // 2
		if x in seen:
			return False
		seen.add(x)
	return True


n = int(input())
if sum_of_four_squares(n):
	print(4)
elif sum_of_three_squares(n):
	print(3)
elif sum_of_two_squares(n):
	print(2)
else:
	print(1)