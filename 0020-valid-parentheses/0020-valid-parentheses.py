class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for c in s:
            if c in pairs.keys():
                stack.append(c)
            else:
                if not stack or c != pairs[stack[-1]]:
                    return False
                stack.pop()
            
        if not stack:
            return True
        return False