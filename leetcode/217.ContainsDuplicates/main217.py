class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 0
            else:
                return True
        return False