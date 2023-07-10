input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

MAX_LEN_N = 30 # log2(MAX_N)

class TrieNode:
    def __init__(self, words = []):
        self.nodes: dict[str, TrieNode] = {}
        self.is_leaf = False
        for word in words:
            self.insert(word)

    def insert(curr, word):
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True
        
def solve(curr, S):
    ret = ""
    for s in S:
        find = "1" if s == "0" else "0"
        if find in curr.nodes:
            ret += "1"
            curr = curr.nodes[find]
        else:
            ret += "0"
            curr = curr.nodes[s]
            
    return int(ret, 2)

N = inp()
A = inl()

root = TrieNode()

for i in range(N):
    a = A[i]
    
    A[i] = bin(A[i])[2:]
    A[i] = "0" * (MAX_LEN_N - len(A[i])) + A[i]
    
    root.insert(A[i])

ans = 0
for a in A:
    ans = max(ans, solve(root, a))
print(ans)