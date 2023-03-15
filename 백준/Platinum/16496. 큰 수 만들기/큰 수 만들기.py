import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int,input().split()))

numbers = [str(i) for i in a]
numbers.sort(key=lambda x: (x*10)[:10], reverse=True)

if numbers[0] == '0':
    answer = '0'
else:
    answer = ''.join(numbers)

print(answer)