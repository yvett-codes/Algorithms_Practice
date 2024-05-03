'''
Status: Complete
Progress: 58/58 Tests Passing
Refactored: NO
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:    
        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        return False