import sys
def input(): return sys.stdin.readline().rstrip()

def Bnp(balance):
    global stockprice
    
    stocks = 0
    
    for i in range(14):
        stocks += balance // stockprice[i]
        balance = balance % stockprice[i]
        
    res = balance + stockprice[-1] * stocks
    return res

def Timing(balance):
    global stockprice
    
    stocks = 0
    
    for i in range(2,14):
        if stockprice[i] < stockprice[i-1] < stockprice[i-2] < stockprice[i-3]:
            stocks += balance // stockprice[i]
            balance = balance % stockprice[i]
        if stockprice[i] > stockprice[i-1] > stockprice[i-2] > stockprice[i-3]:
            balance += stockprice[i]*stocks
            stocks = 0
        
    res = balance + stockprice[-1] * stocks
    return res

balance=int(input())
stockprice = list(map(int, input().split()))

if Bnp(balance) > Timing(balance): print("BNP")
elif Bnp(balance) < Timing(balance): print("TIMING")
else: print("SAMESAME")