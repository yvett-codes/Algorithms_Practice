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
    


# Testing Examples
solution = Solution()

# Pass
nums = [1, 2, 3, 1]
k = 3
result1 = solution.containsNearbyDuplicate(nums, k)
print(f"Case 1: {result1}")  # True
assert result1 == True

# Pass
nums = [1, 0, 1, 1]
k = 1
result2 = solution.containsNearbyDuplicate(nums, k)
print(f"Case 2: {result2}")  # True
assert result2 == True

# Pass
nums = [1, 2, 3, 1, 2, 3]
k = 2
result3 = solution.containsNearbyDuplicate(nums, k)
print(f"Case 3: {result3}")  # False
assert result3 == False

# Pass
nums = [99, 99]
k = 2
result4 = solution.containsNearbyDuplicate(nums, k)
print(f"Case 4: {result4}")  # True
assert result4 == True

# Pass
nums = [2, 2]
k = 3
result5 = solution.containsNearbyDuplicate(nums, k)
print(f"Case 5: {result5}")  # True
assert result5 == True

# Pass
nums = [1,1,3,4,5,6]
k = 7
result6 = solution.containsNearbyDuplicate(nums, k)
print(f"Case 6: {result6}")  # True
assert result6 == True