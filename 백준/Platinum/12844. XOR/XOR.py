import sys
input = lambda: sys.stdin.readline().rstrip()
import math

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start+end)//2
        init(a, tree, node*2, start, mid)
        init(a, tree, node*2+1, mid+1, end)
        tree[node] = tree[node*2] ^ tree[node*2+1]

def update_lazy(tree, lazy, node, start, end):
    if lazy[node] != 0:
        if (end-start+1) & 1:
            tree[node] ^= lazy[node]
        if start != end:
            lazy[node*2] ^= lazy[node]
            lazy[node*2+1] ^= lazy[node]
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right, diff):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        if (end-start+1) & 1:
            tree[node] ^= diff
        if start != end:
            lazy[node*2] ^= diff
            lazy[node*2+1] ^= diff
        return
    mid = (start+end)//2
    update_range(tree, lazy, node*2, start, mid, left, right, diff)
    update_range(tree, lazy, node*2+1, mid+1, end, left, right, diff)
    tree[node] = tree[node*2] ^ tree[node*2+1]

def query(tree, lazy, node, start, end, left, right):
    update_lazy(tree, lazy, node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start+end)//2
    lside = query(tree, lazy, node*2, start, mid, left, right)
    rside = query(tree, lazy, node*2+1, mid+1, end, left, right)
    return lside ^ rside

n = int(input())
a = list(map(int,input().split()))
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [0] * tree_size
lazy = [0] * tree_size
init(a, tree, 1, 0, n-1)
for _ in range(int(input())):
    what, *q = map(int, input().split())
    if what == 1:
        left, right, diff = q
        update_range(tree, lazy, 1, 0, n-1, left, right, diff)
    else:
        left, right = q
        print(query(tree, lazy, 1, 0, n-1, left, right))