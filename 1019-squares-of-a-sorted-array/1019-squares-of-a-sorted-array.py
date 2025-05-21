class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        sqrs = []

        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                sqrs.append(nums[l] ** 2)
                l += 1
            else:
                sqrs.append(nums[r] ** 2)
                r -= 1

        return sqrs[::-1]

        # Time: O(n)
        # Space: O(1)