class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_s = []

        for a, b in zip_longest(word1, word2, fillvalue=""):
            merged_s.append(a)
            merged_s.append(b)

        return "".join(merged_s)