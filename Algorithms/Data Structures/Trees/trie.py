class TrieNode:
    def __init__(self, *words):
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
        
    def find(curr, word):
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def delete(self, word):
        def _delete(curr, word, idx):
            if idx == len(word):
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0
            char = word[idx]
            char_node = curr.nodes.get(char)
            if not char_node:
                return False
            delete_curr = _delete(char_node, word, idx + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_curr
        _delete(self, word, 0)

    def __repr__(self, word = ""):
        words = []
        def _print_words(node, word):
            if node.is_leaf:
                words.append(word)
            for key, value in node.nodes.items():
                _print_words(value, word + key)
        _print_words(self, "")
        return " ".join(words)

words = "banana bananas bandana band apple all beast".split()
root = TrieNode(words)
print(root)
