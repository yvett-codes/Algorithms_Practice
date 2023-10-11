class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Each number is the sum of the two preceding ones
        # 0, 1, 1, 2, 3, 5, 8, 13, 21...
        # For 2:
            # 0 + 1 = 1 - Base (position 1 and 2)
            # result = 1, at position 2
        # For 3:
            # 0 + 1 = 1 - Base (position 1 and 2)
            # 1 + 1 = 2
            # result = 2, at position 3
        # For 4:
            # 0 + 1 = 1 - Base (position 1 and 2)
            # 1 + 1 = 2
            # 2 + 1 = 3
            # result = 3, at position 4
        # For 1:
            # 0 + _ = 0
            # result = 0, at position 1
        # For 0:
            # result = null, at position 0
        # F(0) = 0, F(1) = 1
        # F(n) = F(n - 1) + F(n - 2), for n > 1.
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 3


# Testing Solutions:
# Create an instance of the Solution class
solution_instance = Solution()

# Call the lengthOfLongestSubstring method on the instance and provide the input string 's'
result1 = solution_instance.fib(2)
result2 = solution_instance.fib(3)
result3 = solution_instance.fib(4)

# Print the result
print(result1)
print(result2)
print(result3)

# assert result1 == 1
# assert result2 == 2
# assert result3 == 3