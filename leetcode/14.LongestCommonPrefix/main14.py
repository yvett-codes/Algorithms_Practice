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
        """
        Returns if the word is in the trie.
        """

    def startsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # make a hash table?

    # isEndOfWord is True if node represent the end of the word

