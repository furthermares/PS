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
        tree[node] = tree[node*2] + tree[node*2+1]

def update_lazy(tree, lazy, node, start, end):
    if lazy[node]:
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right, diff):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    mid = (start+end)>>1
    update_range(tree, lazy, node*2, start, mid, left, right, diff)
    update_range(tree, lazy, node*2+1, mid+1, end, left, right, diff)
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

n = int(input())
a = [0] + list(map(int,input().split()))
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
lazy = [0] * tree_size

for i in range(1,n+1):
    update_range(tree, lazy, 1, 1, n, i, i, a[i]-a[i-1])

for _ in range(int(input())):
    what, *q = map(int, input().split())
    if what == 1:
        left, right = q
        update_range(tree, lazy, 1, 1, n, left, right, 1)
        update_range(tree, lazy, 1, 1, n, right+1, right+1, -(right-left+1))
    else:
        k = q[0]
        print(query(tree, lazy, 1, 1, n, 1, k))