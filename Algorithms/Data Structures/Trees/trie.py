class TrieNode:
    def __init__(self):
        self.nodes: dict[str, TrieNode] = {} # Mapping from char to TrieNode
        self.is_leaf = False

    def insert(curr, word):
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
        curr.is_leaf = True
        
    def find(curr, word) -> bool:
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        return curr.is_leaf

    def delete(self, word):
        def _delete(curr, word, idx):
            if idx == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                return len(curr.nodes) == 0
            char = word[idx]
            char_node = curr.nodes.get(char)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, idx + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            return delete_curr

        _delete(self, word, 0)

    def print(self, word = ""):
        def _print_words(node, word):
            if node.is_leaf:
                print(word, end=" ")
        
            for key, value in node.nodes.items():
                _print_words(value, word + key)

        _print_words(self, "")

words = "banana bananas bandana band apple all beast".split()
root = TrieNode()
for word in words:
    root.insert(word)
root.print()
