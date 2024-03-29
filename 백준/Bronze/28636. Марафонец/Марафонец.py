t=sum(s+m*60for m,s in[map(int,input().split(":"))for _ in[0]*int(input())])
print(f"{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}")