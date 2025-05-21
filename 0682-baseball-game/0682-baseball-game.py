class Solution:
    def calPoints(self, operations: List[str]) -> int:
        totals = []

        for x in operations:
            if not x.isalpha() and x != '+':
                    totals.append(int(x))

            if x == '+':
                totals.append(totals[-2] + totals[-1])
            elif x == 'D':
                totals.append(totals[-1] * 2)
            elif x == 'C':
                totals.pop()

        return sum (totals)

        # iterate through ops
        # for char, if char is an int, add that to our stack
            # totals.append(x)
        # qualify our chars according to conditions
        # return the sum of the array
        '''
        if x == '+':
            totals.append(totals[-2] + totals[-1])
        elif x == 'D':
            totals.append(totals[-1] * 2)
        elif x == 'C':
            totals.pop()

        return sum (totals)
        '''
        

        # Time: O(n)
        # Space: O(n)