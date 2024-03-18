'''
Status: In Progress
Progress: -
Refactored: NO
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = [int(n) for n in a]
        d = [int(n) for n in b]
        c = c[::-1]
        d = d[::-1]

        result = []
        carry = 0

        if len(c) > len(d):
            diff = len(c) - len(d)
            for i in range(diff):
                d.append(0)
        else:
            diff = len(d) - len(c)
            for i in range(diff):
                d.append(0)

        for i in range(len(c)):
            sum = c[i] + d[i] + carry
            if sum == 0:
                result.append(0)
                carry = 0
            elif sum == 1:
                result.append(1)
                carry = 0
            elif sum == 2:
                result.append(0)
                carry = 1
            else:
                result.append(1)
                carry = 1

        if carry:
            result.append(1)

        result = result[::-1]        
        result  = ''.join(str(x) for x in result)
        return result
    
solution = Solution()

solution.addBinary()