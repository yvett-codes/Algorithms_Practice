from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = defaultdict(int)

        for m in magazine:
            m_dict[m] += 1

        for r in ransomNote:
            if not m_dict[r]:
                return False
            m_dict[r] -= 1
        return True

        # Time: O(n + m)
        # Space: O(1)