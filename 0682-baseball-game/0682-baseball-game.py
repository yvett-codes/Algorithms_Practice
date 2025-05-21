class Solution:
    def calPoints(self, operations: List[str]) -> int:
        totals = []

        for x in operations:
            if x.strip('-').isdigit():
                totals.append(int(x))
            elif x == '+':
                totals.append(totals[-2] + totals[-1])
            elif x == 'D':
                totals.append(totals[-1] * 2)
            elif x == 'C':
                totals.pop()

        return sum (totals)        

        # Time: O(n)
        # Space: O(n)