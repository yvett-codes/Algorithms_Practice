class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        num = nums[0]
        for n in nums:
            if abs(n) < abs(num):
                num = n
        if num < 0 and abs(num) in nums:
            return abs(num)
        return num

        # Time: O(n)
        # Space: O(1)
