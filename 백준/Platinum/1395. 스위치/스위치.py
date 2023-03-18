import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def update_lazy(tree, lazy, node, start, end):
    if lazy[node]:
        tree[node] = (end-start+1) - tree[node]
        if start != end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] = (end-start+1) - tree[node]
        if start != end:
            lazy[node*2] ^= 1
            lazy[node*2+1] ^= 1
        return
    mid = (start+end)>>1
    update_range(tree, lazy, node*2, start, mid, left, right)
    update_range(tree, lazy, node*2+1, mid+1, end, left, right)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, lazy, node, start, end, left, right):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)>>1
    lsum = query(tree, lazy, node*2, start, mid, left, right)
    rsum = query(tree, lazy, node*2+1, mid+1, end, left, right)
    return lsum + rsum

n, m = map(int, input().split())
a = [0] * n
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
lazy = [0] * tree_size
for _ in range(m):
    what, left, right = map(int, input().split())
    if what == 0:
        update_range(tree, lazy, 1, 0, n-1, left-1, right-1)
    else:
        print(query(tree, lazy, 1, 0, n-1, left-1, right-1))