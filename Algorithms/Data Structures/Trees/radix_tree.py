# https://github.com/TheAlgorithms/Python/blob/master/data_structures/trie/radix_tree.py

class RadixNode:
    def __init__(self, prefix = "", is_leaf = False):
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

    def insert_many(self, words):
        for word in words:
            self.insert(word)

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

    def find(self, word):
        incoming_node = self.nodes.get(word[0], None)
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(word)
            
            if remaining_prefix != "":
                return False
            
            elif remaining_word == "":
                return incoming_node.is_leaf
            
            else:
                return incoming_node.find(remaining_word)

    def delete(self, word):
        incoming_node = self.nodes.get(word[0], None)
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(word)
            
            if remaining_prefix != "":
                return False
            
            elif remaining_word != "":
                return incoming_node.delete(remaining_word)
            
            else:
                if not incoming_node.is_leaf:
                    return False
                else:
                    if len(incoming_node.nodes) == 0:
                        del self.nodes[word[0]]
                        
                        if len(self.nodes) == 1 and not self.is_leaf:
                            merging_node = list(self.nodes.values())[0]
                            self.is_leaf = merging_node.is_leaf
                            self.prefix += merging_node.prefix
                            self.nodes = merging_node.nodes
                    
                    elif len(incoming_node.nodes) > 1:
                        incoming_node.is_leaf = False
                    
                    else:
                        merging_node = list(incoming_node.nodes.values())[0]
                        incoming_node.is_leaf = merging_node.is_leaf
                        incoming_node.prefix += merging_node.prefix
                        incoming_node.nodes = merging_node.nodes

                    return True

    def print_tree(self, height = 0):
        if self.prefix != "":
            print("-" * height, self.prefix, "  (leaf)" if self.is_leaf else "")

        for value in self.nodes.values():
            value.print_tree(height + 1)
        for value in self.nodes.values():
            value.print_tree(height + 1)

        return print_lst

    def __repr__(self): # trick. Doesn't actually do what it's supposed to do.
        self.print_tree()
        return ""
