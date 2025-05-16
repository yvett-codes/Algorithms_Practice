from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_dict = defaultdict(int)

        for m in magazine:
            m_dict[m] += 1


        for r in ransomNote:
            if r not in m_dict:
                return False
            else:
                m_dict[r] -= 1
                if not m_dict[r]:
                    del m_dict[r]
        return True