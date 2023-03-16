def solution(n):
    fibonacci = [1, 2]
    for i in range(2, n):
        fibonacci.append((fibonacci[i-1] + fibonacci[i-2]) % 1000000007)
    return fibonacci[n - 1]