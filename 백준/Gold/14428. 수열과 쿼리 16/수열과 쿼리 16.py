import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def min(a,b):
    return b if a[0] > b[0] else a

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
        return [sys.maxsize,sys.maxsize]
    if start == end:
        return
    mid = (start+end)>>1
    update(a, tree, node*2, start, mid, index, val)
    update(a, tree, node*2+1, mid+1, end, index, val)
    tree[node] = min(tree[node*2], tree[node*2+1])
    
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return [sys.maxsize, sys.maxsize]
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)>>1
    lside = query(tree, node*2, start, mid, left, right)
    rside = query(tree, node*2+1, mid+1, end, left, right)
    return min(lside,rside)

n = int(input())
tmp = list(map(int,input().split()))
a = [[tmp[i],i+1] for i in range(n)]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
init(a, tree, 1, 0 , n-1)
for _ in range(int(input())):
    what, t1, t2 = map(int, input().split())
    if what == 1:
        index, val = t1, t2
        a[index - 1][0] = val
        update(a, tree, 1, 0, n-1, index-1, val)
    else:
        left, right = t1, t2
        print(query(tree, 1, 0, n-1, left-1, right-1)[1])