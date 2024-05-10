input=__import__('sys').stdin.readline
inp=lambda:int(input())
ins=lambda:input().rstrip()
__import__('sys').setrecursionlimit(10**6)

class TrieNode:
    def __init__(self, words = []):
        self.nodes: dict[str, TrieNode] = {} # Mapping from char to TrieNode
        self.is_leaf = False
        for word in words:
            self.insert(word)

    def insert(curr, word):
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True

    def print(self, word = ""):
        def _print_words(node, word, depth):
            if word: print(word)
            if node.is_leaf:
                pass
            for key, value in sorted(node.nodes.items()):
                _print_words(value, "--"*depth + key, depth+1)
        _print_words(self, "", 0)

root = TrieNode()
for _ in range(inp()):
    root.insert(ins()[2:].split())
root.print()