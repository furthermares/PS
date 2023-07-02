input = __import__('sys').stdin.readline
inp = lambda: int(input())
ins = lambda: input().rstrip()

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

def num_of_branches(curr, word):
    cnt = 0
    for w in word:
        curr = curr.nodes[w]
        if len(curr.nodes) > 1 or curr.is_leaf:
            cnt += 1
    return cnt

try:
    while True:
        N = inp()
        S = [ins() for _ in range(N)]
        
        root = TrieNode(S)
        
        res = 0
        for s in S:
            res += num_of_branches(root, s)
        
        print("%.2f"%(res/N))
except:
    exit(0)