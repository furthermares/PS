for _ in[0]*int(input()):
    input()
    P,Q=input(),input()

    if P==Q:
        print("*")
        continue

    for i in range(min(len(P),len(Q))):
        if P[i]!=Q[i]:
            idx=i
            break
    else:
        idx=min(len(P),len(Q))
        
    if(len(Q)>idx*2):
        print(f"*{P}*")
    else:
        print("<"*(len(Q)-idx)+P[idx:]+"*")