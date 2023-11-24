input=__import__('sys').stdin.readline
while N:=int(input()):print(["SIM","NAO"][N&~-N==0and N!=0])