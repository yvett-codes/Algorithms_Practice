class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = {j:0 for j in jewels}

        for s in stones:
            if s in jewels:
                jewels[s] += 1
        
        sum = 0
        for val in jewels.values():
            sum += val
        return sum