class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        comp = abs(nums[0])
        result = nums[0]
        for n in nums:
            if abs(n) < comp:
                result, comp = n, abs(n)

        if abs(result) in nums:
            return abs(result)
        return result