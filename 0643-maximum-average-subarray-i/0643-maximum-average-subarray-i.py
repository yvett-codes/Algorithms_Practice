class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(len(nums) - k):
            window_sum += nums[i + k] - nums[i]
            if window_sum > max_sum:
                max_sum = window_sum
        
        return max_sum / k

        # Time: O(n)
        # Space: O(1)