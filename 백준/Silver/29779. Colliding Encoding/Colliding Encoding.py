I=__import__('sys').stdin.readline
for T in range(int(I())):
 D,S,N=I().split(),set(),int(I())
 for _ in[0]*N:
  s=I()
  for i in range(26):s=s.replace(chr(i+65),D[i])
  S.add(s)
 print(f"Case #{T+1}:",["YES","NO"][len(S)==N])