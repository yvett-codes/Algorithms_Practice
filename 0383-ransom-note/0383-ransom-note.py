class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_list = list(ransomNote)
        m_list = list(magazine)

        for l in r_list:
            if l in m_list:
                m_list.remove(l)
            else:
                return False
        return True
