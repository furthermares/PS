import sys
input = lambda: sys.stdin.readline().rstrip()
import math
MOD = 1000000007

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start+end)>>1
        init(a, tree, node*2, start, mid)
        init(a, tree, node*2+1, mid+1, end)
        tree[node] = (tree[node*2] * tree[node*2+1]) % MOD
        
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
    tree[node] = (tree[node*2] * tree[node*2+1]) % MOD
    
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)>>1
    lside = query(tree, node*2, start, mid, left, right)
    rside = query(tree, node*2+1, mid+1, end, left, right)
    return (lside * rside) % MOD

n, m, k = map(int,input().split())
a = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
init(a, tree, 1, 0 , n-1)
for _ in range(m + k):
    what, t1, t2 = map(int, input().split())
    if what == 1:
        index, val = t1, t2
        update(a, tree, 1, 0, n-1, index-1, val)
    else:
        left, right = t1, t2
        print(query(tree, 1, 0, n-1, left-1, right-1))