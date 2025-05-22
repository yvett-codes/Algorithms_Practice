class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []

        for o in tokens:
            if o.strip('-').isdigit():
                stck.append(int(o))
            # print(stck)

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
                if result > 0:
                    stck.append(math.floor(result))
                else:
                    stck.append(math.ceil(result))
        return sum(stck)