# 242.Valid Anagram  | Python Implementation

## Goals
<!-- Describe your goals to solve this problem. -->
Given two strings, return true if the two strings are anagrams of each other. If the two strings are not, we return false. In order for the strings to be anagrams, the words needs to be formed using all of the letters of the original word exactly once.

## Approach
<!-- Describe your approach to solving the problem. -->
I'd like to utilize hashmaps to keep track of the frequencies of each letter. First, I'll make a hashmap of the first string, ```s```, where the key is the letter and the value is the number of times that letter appears in the word.<br><br>

Next, I'll take the second string, ```t```, and iterate each letter in comparison to the keys in my new hashmap. To keep track of the frequencies of each letter, I will decrement the value of the key *if* the letter in string ```t``` matches that key. If the letter from string ```t``` does not appear in my hashmap, I'll return early with a value of ```False``` because this means that the strings are not anagrams.<br><br>

The goal is for the nominal case to result in a hashmap where each key contains a value of ```0```- this indicates that the two strings have an equal number of occurrences for each letter contained in the string.  If I'm able to make it through the second loop without returning early, then I will proceed by checking if the all of the keys in my hashmap evaluate to a ```False``` value. If all of the keys satisfy this check, then this means the input strings are anagrams and we can return ```True``` as the final output for the function ```isAnagram()```. However, if any of the keys have a value of ```True```, then this means that we have satisfied our requirements for anagrams and the two strings have unqequal frequencies of letter.

## Code
```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for i in s:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for j in t:
            if j not in my_dict:
                return False
            else:
                my_dict[j] -= 1

        for key in my_dict.keys():
            if my_dict[key]:
                return False
        return True
```

## Big O

### Time Complexity
1. Identify data structures which can have variable size.
    There are two data structures that have variable size, ```s``` and ```t```, which both have a size of *n*.
    <br>

2. Identify all the operations (steps) in the algorithm.
    ```my_dict = {}```<br>
    ```for i in s```<br>
    ```if i not in my_dict```<br>
    ```my_dict[i] = 1```<br>
    ```my_dict[i] += 1```<br>
    ```for j in t```<br>
    ```if j not in my_dict```<br>
    ```my_dict[j] -= 1```<br>
    ```for key in my_dict.keys()```<br>
    ```if my_dict[key]```<br>
    <br>

3. Recognize which operations depend on the size of the data structure of size *n*.
    ```for i in s``` ➡️ **n**<br>
    ```for j in t``` ➡️ **n**<br>
    <br>

4. Create an equation that represents how many operations get performed and use *n* as a variable.
    ```my_dict = {}``` ➡️ **1**<br>
    ```for i in s``` ➡️ **n**<br>
    ```if i not in my_dict``` ➡️ **1**<br>
    ```my_dict[i] = 1``` ➡️ **1**<br>
    ```my_dict[i] += 1``` ➡️ **1**<br>
    ```for j in t``` ➡️ **n**<br>
    ```if j not in my_dict``` ➡️ **1**<br>
    ```my_dict[j] -= 1``` ➡️ **1**<br>
    ```for key in my_dict.keys()``` ➡️ **n**<br>
    ```if my_dict[key]``` ➡️ **1**<br>
    <br> ➡️ 1 + n + 1 + 1 + 1 + n + 1 + 1 + n + 1 ➡️ 7 + 3n
    <br>

5. Drop all constants and find the dominant term.
    ➡️ 7 + 3n ➡️ 3n ➡️ n
    <br>

6. Match this to the most relevant complexity.
    n ➡️ **O(n) - Linear Time**<br>
    <br>*The algorithm will grow in time directly proportional to the input size. The complexity increases at the same rate that the input increases.*
    <br>


### Space complexity:
1. Identify all places where a variable is initialized.
    ```my_dict = {}```<br>
    ```for i in s```<br>
    ```my_dict[i] = 1```<br>
    ```for j in t```<br>
    <br>

2. Recognize which variables have a value that could take a variable amount of memory.
    ```my_dict = {}```<br>
    <br>

3. Create an equation that represents how many values are initialized and stored in memory.
    ```my_dict = {}``` ➡️ **n**<br>
    ```for i in s``` ➡️  **1**<br>
    ```my_dict[i] = 1``` ➡️  **1**<br>
    ```for j in t``` ➡️  **1**<br>
    <br> ➡️ n + 1 + 1 + 1 ➡️ n + 3
    <br>

4. Drop all constants and find the dominant term.
    ➡️ n + 3 ➡️ n
    <br>

5. Match this to the most relevant complexity.
    1 ➡️ **O(n) - Linear Space**<br>
    <br>*The algorithm will grow in space directly proportional to the input size. The complexity increases at the same rate that the input increases.*
    <br>