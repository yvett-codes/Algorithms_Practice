'''
Status: Complete
Progress: 63/63 Tests Passing
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {i: nums[i] for i in range(len(nums))}

        for i in nums_dict.keys():
            for j in nums_dict.keys():
                if i == j:
                    continue
                if nums_dict[i] + nums_dict[j] == target:
                    return [i, j]