input = __import__('sys').stdin.readline
inp = lambda: int(input())
ins = lambda: input().rstrip()

class TrieNode:
    def __init__(self):
        self.nodes: dict[str, TrieNode] = {}

        self.delN = False
        self.delT = False
        self.delT_leaf = False

    def insert(curr, word, flag):
        for i in range(len(word)):
            char = word[i]
            
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
            
            if flag:
                curr.delN = True
            else:
                curr.delT = True
            if not flag and i == len(word) - 1:
                curr.delT_leaf = True
                
        curr.is_leaf = True
        
def solve(node):
    ret = 0
    for char in node.nodes:
        curr = node.nodes[char]
        if curr.delT:
            if not curr.delN:
                ret += 1
            if curr.delN and curr.delT_leaf:
                ret += 1
            if curr.delN:
                ret += solve(curr)
    return ret

for _ in range(inp()):
    root = TrieNode()

    N1 = inp()
    for _ in range(N1):
        root.insert(ins(), False)
    N2 = inp()
    for _ in range(N2):
        root.insert(ins(), True)

    res = solve(root)

    print(res) if N2 else print(1)