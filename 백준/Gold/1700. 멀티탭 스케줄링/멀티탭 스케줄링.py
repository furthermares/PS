input = __import__('sys').stdin.readline
inm = lambda: map(int,input().split())
inl = lambda: list(map(int,input().split()))

import heapq

N,K = inm()
A = inl()

if N >= K:
    print(0)
    exit()

idxes = [[] for _ in range(K+1)]
for i in range(K):
    idxes[A[i]].append(i)
heapq.heapify(sockets := [])
in_use = [False] * (K+1)
num_of_used_plugs = [0] * (K+1)
next_plug = 0
cnt = 0
ans = 0

for i in range(K):
    plug = A[i]

    if cnt == N and not in_use[plug]:
        in_use[heapq.heappop(sockets)[1]] = False
        ans += 1
        cnt -= 1
    
    if num_of_used_plugs[plug] == len(idxes[plug])-1:
        next_plug = K+1
    else:
        num_of_used_plugs[plug] += 1
        next_plug = idxes[plug][num_of_used_plugs[plug]]

    if not in_use[plug]:
        cnt += 1
        in_use[plug] = True
    heapq.heappush(sockets, (-next_plug, plug))

print(ans)