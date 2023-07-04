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

def leaf_has_children(curr, word):
    for w in word:
        curr = curr.nodes[w]

    if curr.nodes:
        return True
    return False

for _ in range(inp()):
    N = inp()
    S = [ins() for _ in range(N)]

    root = TrieNode(S)
    
    ans = True
    for s in S:
        if leaf_has_children(root, s):
            ans = False

    print("YES") if ans else print("NO")