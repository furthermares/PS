S=input()
S+="..."
ans=""

i=0
while i < len(S)-3:
    if S[i:i+4].count("X") == 4:
        ans+="AAAA"
        i+=4
    elif S[i:i+2].count("X") == 2:
        ans+="BB"
        i+=2
    elif S[i] == "X" and S[i+1] == ".":
        ans=-1
        break
    elif S[i] == ".":
        ans+="."
        i+=1
        continue
    
print(ans)