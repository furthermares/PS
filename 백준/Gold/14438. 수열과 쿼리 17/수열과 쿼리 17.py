import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start+end)>>1
        init(a, tree, node*2, start, mid)
        init(a, tree, node*2+1, mid+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])
        
def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    mid = (start+end)>>1
    update(a, tree, node*2, start, mid, index, val)
    update(a, tree, node*2+1, mid+1, end, index, val)
    tree[node] = min(tree[node*2], tree[node*2+1])
    
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)>>1
    lmin = query(tree, node*2, start, mid, left, right)
    rmin = query(tree, node*2+1, mid+1, end, left, right)
    if lmin == -1:
        return rmin
    elif rmin == -1:
        return lmin
    else:
        return min(lmin, rmin)

n = int(input())
a = list(map(int,input().split()))
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
init(a, tree, 1, 0 , n-1)
m = int(input())
for _ in range(m):
    what, t1, t2 = map(int, input().split())
    if what == 1:
        index, val = t1, t2
        update(a, tree, 1, 0, n-1, index-1, val)
    else:
        left, right = t1, t2
        print(query(tree, 1, 0, n-1, left-1, right-1))