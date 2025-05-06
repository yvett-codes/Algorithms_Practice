class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        merged_s = ""

        while p < len(word1) and p < len(word2):
            merged_s += word1[p]
            merged_s += word2[p]
            p += 1

        merged_s += word1[p:] if word1 else ""
        merged_s += word2[p:] if word2 else ""

        return merged_s