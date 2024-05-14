'''
Status: Complete
Progress: 63/63 Tests Passing
2 Implentations Included
'''

class Solution:
    # Implementation #1
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {i: nums[i] for i in range(len(nums))}

        for i in nums_dict.keys():
            for j in nums_dict.keys():
                if i == j:
                    continue
                if nums_dict[i] + nums_dict[j] == target:
                    return [i, j]

    # Implementation #2
    def twoSum(self, nums: list[int], target: int) -> list[int]:
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