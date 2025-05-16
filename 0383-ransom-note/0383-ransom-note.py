from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = defaultdict(int)

        for m in magazine:
            m_dict[m] += 1

        for r in ransomNote:
            if m_dict[r] == 0:
                return False
            m_dict[r] -= 1
        return True