# 3. Longest Substring Without Repeating Characters
# This solution was created with Chris.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # start w first letter & add 2nd
        # iterate through s
        # make a new subs to start comparing
#

        # sliding window: start at beginning
        subs = ""
        slen = 0
        for i in range(len(s)):
            while s[i] in subs:
                # use a hashtable, or set -> O(1)
                # solve in c++
            # recalculate len
            # check if that's a reoccur char
                subs = subs[1:]
            subs += s[i]
            # check if longest subs
            # take len of cur compare to slen
            if len(subs) > slen:
                slen = len(subs)
        return slen
    

# Testing Solutions:
# Create an instance of the Solution class
solution_instance = Solution()

# Call the lengthOfLongestSubstring method on the instance and provide the input string 's'
result = solution_instance.lengthOfLongestSubstring("abcabcbb")

# Print the result
print(result)

# lengthOfLongestSubstring("abcabcbb")
# "bbbbb"
# "pwwkew"