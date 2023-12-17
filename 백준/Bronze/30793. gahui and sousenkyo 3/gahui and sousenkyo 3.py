P,R=map(int,input().split())
V,p=P/R,print
if V<.2:p("weak")
elif V<.4:p("normal")
elif V<.6:p("strong")
else:p("very strong")