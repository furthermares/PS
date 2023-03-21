import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def init1(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start+end)>>1
        init1(a, tree, node*2, start, mid)
        init1(a, tree, node*2+1, mid+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])
        
def update1(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    mid = (start+end)>>1
    update1(a, tree, node*2, start, mid, index, val)
    update1(a, tree, node*2+1, mid+1, end, index, val)
    tree[node] = min(tree[node*2], tree[node*2+1])
    
def query1(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)>>1
    lmin = query1(tree, node*2, start, mid, left, right)
    rmin = query1(tree, node*2+1, mid+1, end, left, right)
    if lmin == -1:
        return rmin
    elif rmin == -1:
        return lmin
    else:
        return min(lmin, rmin)

def init2(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start+end)>>1
        init2(a, tree, node*2, start, mid)
        init2(a, tree, node*2+1, mid+1, end)
        tree[node] = max(tree[node*2], tree[node*2+1])
        
def update2(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    mid = (start+end)>>1
    update2(a, tree, node*2, start, mid, index, val)
    update2(a, tree, node*2+1, mid+1, end, index, val)
    tree[node] = max(tree[node*2], tree[node*2+1])
    
def query2(tree, node, start, end, left, right):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)>>1
    lmin = query2(tree, node*2, start, mid, left, right)
    rmin = query2(tree, node*2+1, mid+1, end, left, right)
    if lmin == -1:
        return rmin
    elif rmin == -1:
        return lmin
    else:
        return max(lmin, rmin)
        
n, m = map(int,input().split())
a1 = [int(input()) for _ in range(n)]
a2 = a1[:]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree1 = [0] * tree_size
tree2 = tree1[:]
init1(a1, tree1, 1, 0 , n-1)
init2(a2, tree2, 1, 0 , n-1)

for _ in range(m):
    left, right = map(int, input().split())
    print(query1(tree1, 1, 0, n-1, left-1, right-1), query2(tree2, 1, 0, n-1, left-1, right-1))