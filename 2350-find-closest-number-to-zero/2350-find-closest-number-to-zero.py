class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        abs_value = abs(max(nums))
        value = min(nums)
        print(abs_value, value)
        for n in nums:
            if (abs(n) < abs_value) or (abs(n) == abs_value and n > value):
                abs_value = abs(n)
                value = n
        return value

        # Time: O(n)
        # Space: O(1)