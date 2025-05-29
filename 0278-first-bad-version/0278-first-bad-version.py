# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # n is total number of versions, and n represents the values?
        # go through each and find the lowest bad, where we experience a cross where it's good, bad
        # so if n is an integer, how do i iterate through the array?
        l, r = 0, n
        first = n

        while l <= r:
            mid = l + (r - l) // 2
            bad = isBadVersion(mid)
            if not bad: # too low
                l = mid + 1
            else: # qualifies
                first = mid
                r = mid - 1
        return first