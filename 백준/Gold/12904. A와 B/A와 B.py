input=__import__('sys').stdin.readline
insl=lambda:list(input()[:-1])

S = insl()
T = insl()

while len(T) > len(S):
    if T.pop() == "B":
        T.reverse()
        
print(1) if S == T else print(0)