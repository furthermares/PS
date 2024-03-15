H,L,A,B=map(int,input().split())
print("YNEOS"[((H<A/2)|(L<B))*((H<B/2)|(L<A))::2])