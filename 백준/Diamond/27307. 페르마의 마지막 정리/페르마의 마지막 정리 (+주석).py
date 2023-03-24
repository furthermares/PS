import sys
input = lambda: sys.stdin.readline().rstrip()
from math import gcd
from random import randrange

MOD = 1000000007

# 큰 수 소인수분해 AC 맞은 코드입니다. Witness수 범위 조정 했습니다.
# 69번 줄에서 시작.

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
		
	potential_witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23] # n <= 2e18
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


n, x, y, m = map(int,input().split())
X, Y = abs(x), abs(y)

###
# |x+y|, X, Y 폴라드 로로 소인수분해
Pxy = []
PX = []
PY = []
for P, v in [Pxy, abs(x + y)], [PX, X], [PY, Y]:
    while v > 1:
    	k = PollardRho(v)
    	P.append(k)
    	v //= k

# (a)에서 (b)와 (c) 뺴기. P = P(|x+y|) - P(X) - P(Y)
P = list(set(Pxy).difference(PX, PY))

###
# LTE lemma
# 같은 부호 다른 부호 모두 vpi(x + y) + vpi(n)
f = []
for pi in P:
    vpiXY = 0    # vpi(x + y)
    t = x + y
    while t % pi == 0: # vpi(x + y) = (x+y)안에 pi가 몇제곱까지 있는가
        vpiXY += 1
        t //= pi

    vpin = 0    # vpi(n)
    t = n
    while t % pi == 0:
        vpin += 1
        t //= pi
        
    f.append(vpiXY + vpin)

###
# 2^4 3^2 안에 2^2 3^1의 배수가 m단위로 몇 개 들어가나?
g = []
for fi in f:
    g.append(fi//m)

# 길이 계산 (수식대로)
len_dm = 1
for gi in g:
    len_dm *= 1+gi
    len_dm %= MOD

# 합 계산 (수식대로)
sum_dm = 1
for gi, pi in zip(g, P):
    sum_dm *= (modular_pow(pi, (gi+1)*m, MOD) - 1) // (modular_pow(pi, m, MOD) - 1)
    sum_dm %= MOD

print(len_dm, sum_dm)
