class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}

        for l in s:
            if l in s_dict.keys():
                s_dict[l] += 1
            else:
                s_dict[l] = 1
        
        for l in t:
            if l in s_dict.keys():
                s_dict[l] -= 1
                if s_dict[l] == 0:
                    del s_dict[l]

        return not s_dict