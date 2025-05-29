# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        first = n

        while l <= r:
            mid = l + (r - l) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                first = mid
                r = mid - 1
        
        return first

        # Time: O(logn)
        # Space: O(1)