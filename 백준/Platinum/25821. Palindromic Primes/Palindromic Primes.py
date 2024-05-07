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

L,H=map(int,input().split())

ans=0

for i in (2,3,5,7,11):
  if L <= i <= H: ans += 1

for k in range((len(str(L))-1)//2,min((len(str(H))-1)//2+1,6)):
    for i in range(1, 10**k, 2):
        if i%5 == 0: continue
        b = str(i).zfill(k)
        for j in range(10):
            n = int(b[::-1] + str(j) + b)
            if not L <= n <= H: continue
            if isPrime(n): ans += 1

print(ans)