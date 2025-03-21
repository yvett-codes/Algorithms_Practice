class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        abs_value = abs(max(nums))
        value = min(nums)
        print(abs_value, value)
        for n in nums:
            num = abs(n)
            if num == abs_value and n > value:
                value = n
                abs_value = num
            elif num < abs_value:
                abs_value = num
                value = n
        return value
        