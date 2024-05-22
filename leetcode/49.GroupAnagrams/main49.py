'''
Status: In Progress
Progress: 20/126 Tests Passing
'''

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        '''
        Tags: Array, Hash Table, String, Sorting
        Goal: We're given an aray of strings and we have to group all anagrams together. The output will be a list of lists. Each inner list contains strings of anagrams

        Approach: Well the anagrams can be any arrangement of letters, so that means it's not just forwards and backwards. Should I take each string and find every anagram?
        - I could take the first string, develop anagrams, and then remove any matching in the remaining list?
        - Is this going to require a helper function where I need to check if there is an anagram *first*? Oy vey, this sounds like a lot of steps, I'm not sure the best way to approach this.
        - How can I use a hash table to solve this problem?
            - It wouldn't make any sense to have the strings all as keys
            - I feel like I would have to make a hash table of anagrams for the first string, but what if there is a word included that isn't an anagram at all? Can I assume that all of the inputs are anagrams? damnit there are no hints
            - If I can't figure out a good approach I will have to ask for a hint
            - Right, some of the strings don't have anagrams...
            - I can produce new lists based off of the anagrams, and then add it to the final return value...
            - can i assume that every input string is a real word?

        Example:
            "strs": ["eat","tea","tan","ate","nat","bat"],
            "expected": [["bat"],["nat","tan"],["ate","eat","tea"]]
        '''
        strings = strs[:]
        bigList = []
        for w in strings:
            little_list = [w]
            strings.remove(w)
            for x in strings:
                result = self.checkAnagram(w, x)
                if result:
                    little_list.append(x)
                    strings.remove(x)
            little_list.sort()
            bigList.append(little_list)

        if strings:
            bigList.append([strings[0]])
        
        bigList = sorted(bigList, key=len)
        return bigList
    
    def checkAnagram(self, string1: str, string2: str) -> bool:
        string1_dict = {}
        for l in string1:
            if l in string1_dict:
                string1_dict[l] += 1
            else:
                string1_dict[l] = 1

        for j in string2:
            if j in string1:
                string1_dict[j] -= 1
            else:
                return False
            
        for k in string1_dict.keys():
            if string1_dict[k] > 0:
                return False
        
        return True
    


    


    


    


    


    


# --- TESTING ---

# Helper Functions
def runCases(cases):
    for i in range(len(cases)):
        runCase(i + 1)

def runCase(case):
    print(f"--- Case {case} ---")
    result = solution.groupAnagrams(cases[case - 1]["strs"])
    findResult(cases[case - 1]["strs"], cases[case - 1]["expected"], result)

def findResult(input, expected, result):
    if result == expected:
        print("Pass ✅\n")
    else:
        print("FAIL ❌")    
        print(f"Input: {input}\nExpected: {expected}\nResult: {result}\n")

# Cases
cases = [
    {
        "strs": ["eat","tea","tan","ate","nat","bat"],
        "expected": [["bat"],["nat","tan"],["ate","eat","tea"]]
    },
    {
        "strs": [""],
        "expected": [[""]]
    },
    {
        "strs": ["a"],
        "expected": [["a"]]
    },
    {
        "strs": ["","",""],
        "expected": [["","",""]]
    }
]

# Calls
solution = Solution()
runCases(cases)
# runCase(1)