class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []

        for o in tokens:
            if o.strip('-').isdigit():
                stck.append(int(o))

            if o == '+' and len(stck) >= 2:
                result = stck[-2] + stck[-1]
                stck.pop()
                stck.pop()
                stck.append(result)
            elif o == '-' and len(stck) >= 2:
                result = stck[-2] - stck[-1]
                stck.pop()
                stck.pop()
                stck.append(result)
            elif o == '*' and len(stck) >= 2:
                result = stck[-2] * stck[-1]
                stck.pop()
                stck.pop()
                stck.append(result)
            elif o == '/' and len(stck) >= 2:
                result = stck[-2] / stck[-1]
                stck.pop()
                stck.pop()
                stck.append(math.trunc(result))

        return sum(stck)

        # Time: O(n)
        # Space: O(n)