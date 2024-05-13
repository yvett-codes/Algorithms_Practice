'''
Status: In Progress
Progress: 56/63 Tests Passing
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        '''
        The input nums represents a list of numbers. I'll need to figure out which two numbers in the list add to equal the value of the target.
        I need to return the index placements of these two numbers.

        I *could* do a nested loop, but I feel like that is going to be unhappy. First of all, are there any negative numbers in these lists?
        I have an inclination to first take away any numbers that are larger than the target.
        Then, I'll go ahead and see what's left and see if it adds up to the target.
        '''
        # nums = [n for n in nums if n < target]

        # Hash table?
        '''
        create a key with the index and value is the num
        '''
        nums_dict = {i: nums[i] for i in range(len(nums))}
        # if i make a copy doing the same exact thing, do these have the same space in memory?
        nums_dict2 = {i: nums[i] for i in range(len(nums))}
        # what if I just make it so it's impossible for the first to be the answer?
        nums_dict2[0] = target
        # print(nums_dict)

        for i in nums_dict.keys(): # [3,2,4], i = 0
            for j in nums_dict2.keys(): # [9,2,4], j = 0
                if nums_dict[i] + nums_dict2[j] == target:
                    return [i, j]
        # for i in nums_dict.keys():
        #     for j in nums_dict.keys():
        #         if nums_dict[i] + nums_dict[j] == target:
        #             return [i, j]

        # nums2 = nums[:]
        # for n in nums:
        #     if len(nums2) > 1:
        #         nums2 = nums[1:]
        #     for m in nums2:
        #         if n == m and n + m == target:
        #             n = nums.index(n)
        #             nums[m] = "index2"

        #             # del nums[n]
        #             return [n, nums.index(m)]
        #         elif n + m == target:
        #             return [nums.index(n), nums.index(m)]


# Testing Examples
solution = Solution()

# Pass
nums = [2,7,11,15]
target = 9
result = solution.twoSum(nums, target)
print(f"Actual: {result}, Expected: [0,1]")

# Pass
nums = [3,2,4]
target = 6
result = solution.twoSum(nums, target)
print(f"Actual: {result}, Expected: [1,2]")

# Pass
nums = [3,3]
target = 6
result = solution.twoSum(nums, target)
print(f"Actual: {result}, Expected: [0,1]")