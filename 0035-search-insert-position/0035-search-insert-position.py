class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

        if nums[mid] > target:
            if (mid - 1 >= 0):
                return len(nums[:mid])
            else:
                return 0
        elif nums[mid] <= target:
            return mid + 1