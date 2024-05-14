'''
Status: Complete
Progress: 63/63 Tests Passing
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # nums_dict = {i: nums[i] for i in range(len(nums))}

        # for i in nums_dict.keys():
        #     for j in nums_dict.keys():
        #         if i == j:
        #             continue
        #         if nums_dict[i] + nums_dict[j] == target:
        #             return [i, j]
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if i != j and nums[i] + nums[j] == target:
                return [i, j]
            elif j == len(nums) - 1:
                j = 1
                i += 1
            else:
                j += 1

solution = Solution()

# # Test Case 1
nums = [3,2,4]
target = 6
result = solution.twoSum(nums, target)
print(f"Expected: [1,2], Actual: {result}")

# Test Case 2
nums = [2,7,11,15]
target = 9
result = solution.twoSum(nums, target)
print(f"Expected: [0,1], Actual: {result}")