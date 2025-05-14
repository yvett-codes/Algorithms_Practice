class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)

        total = 0
        for s in stones:
            if s in jewels_set:
                total += 1
        
        return total

        # Time: O(n + m)
        # Space: O(n)