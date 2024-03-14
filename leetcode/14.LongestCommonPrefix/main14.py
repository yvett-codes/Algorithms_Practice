# STATUS: IN PROGRESS

# Trie node class
class TrieNode:
    def __init__(self):
        # We could use an array instead of a hashmap, but dicts are easier
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        # Once the trie node is created, we basically have an empty tree
        self.root = TrieNode()

    # Now we need a way to insert words into the empty tree
    def insert(self, word: str) -> None:
        # We're going to initially start at the root
        cur = self.root

        for c in word:
            # Does this char already exist? If not, create a TrieNode for the character
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
        # if it *does* exist, then we can update the position of cur to the child node of the character
            # why do we need line 33? we are shifting the pointer to the child pointer
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
        # make a hash table?

    # isEndOfWord is True if node represent the end of the word

def print_trie(node, prefix=""):
    if node.isEndOfWord:
        print(prefix)
    
    for char, child in node.children.items():
        print_trie(child, prefix + char)

dictionary = Trie()
dictionary.insert("apple")
dictionary.insert("banana")
dictionary.insert("cat")
dictionary.insert("dog")
dictionary.insert("elephant")
print("Words in dictionary: ")
print(dictionary)
print(dictionary.search)
# print(dictionary.root.children)
# print_trie(dictionary.root)