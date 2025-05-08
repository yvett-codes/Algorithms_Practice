class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = roman_numerals[s[0]]    
        for i in range(1, len(s)):
            if roman_numerals[s[i]] > roman_numerals[s[i - 1]]:
                total -= (roman_numerals[s[i - 1]] * 2)
            total += roman_numerals[s[i]]
        return total

        # Time: O(n)
        # Space: O(1)