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

        sum = 0
        val = roman_numerals[s[0]]
        
        for i in range(len(s)):
            if roman_numerals[s[i]] > val:
                sum -= (roman_numerals[s[i - 1]] * 2)
            val = roman_numerals[s[i]]
            sum += roman_numerals[s[i]]
            print(sum)
        return sum


        # "MCMXCIV"
        # M = 1000
        # C = -100
        # M = 1000
        # X = -10
        # C = 100
        # I = -1
        # V = 5