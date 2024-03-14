# Status: In Progress

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if k > len(nums):
            return False
    
        for i in range(len(nums)):
            if (i+k) < len(nums) and nums[i] in nums[i+1:i+k+1]:
                return True
        return False
    


# Testing Examples
solution = Solution()

# Pass
nums = [1, 2, 3, 1]
k = 3
result = solution.containsNearbyDuplicate(nums, k)
print("Example 1:", result)  # True

# Pass
nums = [1, 0, 1, 1]
k = 1
result = solution.containsNearbyDuplicate(nums, k)
print("Example 2:", result)  # True

# Pass
nums = [1, 2, 3, 1, 2, 3]
k = 2
result = solution.containsNearbyDuplicate(nums, k)
print("Example 3:", result)  # False

# FAIL
nums = [99, 99]
k = 2
result = solution.containsNearbyDuplicate(nums, k)
print("Example 4:", result)  # True