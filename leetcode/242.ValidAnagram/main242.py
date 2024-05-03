'''
Status: Complete
Progress: 48/48 Tests Passing
Refactored: NO
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for i in s:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for j in t:
            if j not in my_dict:
                return False
            else:
                my_dict[j] -= 1

        for key in my_dict.keys():
            if my_dict[key]:
                return False
        return True