'''
Status: In Progress
Progress: 43/48 Tests Passing
Refactored: NO
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        make a hashmap out of the first string
        if the letter is already in the hashmap, add an int
        what about sets and tuples? nahh
        then we compare the second string to the hash map
        substract 1 int for each key
        if all of the keys are false, or at value of 0, then it's an anagram -> return True
        if not, return False
        '''
        my_dict = {}
        for i in s:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        
        print(my_dict)

        for j in t:
            if j not in my_dict:
                return False
            else:
                my_dict[j] -= 1

        print(my_dict)

        for key in my_dict.keys():
            if my_dict[key] == True:
                return False
        return True




solution = Solution()

# Example 1
s="anagram"
t="nagaram"
# result1 = solution.isAnagram(s, t)
# print(f"Expected: True, Actual: {result1}")

# Example 1
s="ab"
t="a"
# result1 = solution.isAnagram(s, t)
# print(f"Expected: False, Actual: {result1}")