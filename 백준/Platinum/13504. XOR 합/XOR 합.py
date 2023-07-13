input = __import__('sys').stdin.readline
inp = lambda: int(input())
inl = lambda: list(map(int,input().split()))

from collections import OrderedDict

class RadixNode:
    def __init__(self, prefix: str = "", is_leaf: bool = False):
        self.nodes = {}
        self.is_leaf = is_leaf
        self.prefix = prefix

    def match(self, word):
        x = 0
        for q, w in zip(self.prefix, word):
            if q != w:
                break
            x += 1
        return self.prefix[:x], self.prefix[x:], word[x:]

    def insert(self, word):            
        if self.prefix == word:
            self.is_leaf = True
            
        elif word[0] not in self.nodes:
            self.nodes[word[0]] = RadixNode(prefix=word, is_leaf=True)

        else:
            incoming_node = self.nodes[word[0]]
            matching_string, remaining_prefix, remaining_word = incoming_node.match(word)

            if remaining_prefix == "":
                self.nodes[matching_string[0]].insert(remaining_word)

            else:
                incoming_node.prefix = remaining_prefix

                aux_node = self.nodes[matching_string[0]]
                self.nodes[matching_string[0]] = RadixNode(matching_string, False)
                self.nodes[matching_string[0]].nodes[remaining_prefix[0]] = aux_node

                if remaining_word == "":
                    self.nodes[matching_string[0]].is_leaf = True
                else:
                    self.nodes[matching_string[0]].insert(remaining_word)


def solve(curr, S):
    ret = ""
    find = ""
    for i in range(len(S)):
        find += "1" if S[i] == "0" else "0"
    i = 0
    while i < len(S):
        for s in curr.prefix:
            if find[i] == s:
                ret += "1"
            else:
                ret += "0"
            i += 1
            
        if curr.is_leaf == True:
            break
            
        if find[i] in curr.nodes:
            curr = curr.nodes[find[i]]
        else:
            curr = curr.nodes[S[i]]
            
    return int(ret, 2)

def remove_duplicates(lst):
    return list(OrderedDict.fromkeys(lst))

for _ in range(inp()):
    N = inp()
    A = [0] + inl()
    
    for i in range(1, N+1):
        A[i] ^= A[i-1]
    
    A = remove_duplicates(A)

    root = RadixNode()

    max_len = len(bin(max(A))) - 2
    for i in range(len(A)):
        A[i] = bin(A[i])[2:]
        A[i] = "0" * (max_len - len(A[i])) + A[i]
        
        root.insert(A[i])

    ans = 0
    for a in A[1:]:
        ans = max(ans, solve(root, a))

    print(ans)