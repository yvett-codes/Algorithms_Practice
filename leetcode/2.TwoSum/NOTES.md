# 2.Two Sum | Python Implementation

## Goals
For our input, we've received an array of integers. We need to return ```true``` if any integer appears at least twice in our array. We will return ```false``` if the array has distinct elements.

## Approach
<!-- Describe your approach to solving the problem. -->
I'd like to keep track of the occurences of each element, so I will utilize a hash map. I'll create a dictionary and loop through our array. If the element is not already in our dictionary, then we'll populate a key, value for the element. If the element is already in our dictionary, we'll return ```true``` because we have discovered that the array is not comprised of entirely unique elements. If we have gotten to the end of the array without triggering the preemptive return, we'll return ```false``` because the array is comprised of unique elements.

## Code
```
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 0
            else:
                return True
        return False
```

## Big O

### Time Complexity
1. Identify data structures which can have variable size.<br>
    There is one array with variable size, ```nums```, and its of size *n*.
    <br>

2. Identify all the operations (steps) in the algorithm.<br>
    ```nums_dict = {}```<br>
    ```for n in nums```<br>
    ```if n not in nums```<br>
    ```nums_dict[n] = 0```<br>
    <br>

3. Recognize which operations depend on the size of the data structure of size *n*.<br>
```for n in nums``` ➡️ **n**<br>
<br>

4. Create an equation that represents how many operations get performed and use *n* as a variable.<br>
    ```nums_dict = {}``` ➡️ **1**<br>
    ```for n in nums``` ➡️ **n**<br>
    ```if n not in nums``` ➡️ **1**<br>
    ```nums_dict[n] = 0``` ➡️ **1**<br>
    <br> ➡️ 1 + n + 1 + 1 ➡️ 3 + n
<br>

5. Drop all constants and find the dominant term.<br>
➡️ 3 + n ➡️ n
<br>

6. Match this to the most relevant complexity.<br>
    n ➡️ **O(n) - Linear Time**<br>
    <br>*The algorithm will grow in time directly proportional to the input size. The complexity increases at the same rate that the input increases.*
<br>


### Space complexity
1. Identify all places where a variable is initialized.<br>
    ```nums_dict = {}```<br>
    ```for n in nums```<br>
    ```nums_dict[n] = 0```<br>
    <br>

2. Recognize which variables have a value that could take a variable amount of memory.<br>
    ```nums_dict = {}```<br>
<br>

3. Create an equation that represents how many values are initialized and stored in memory.<br>
    ```nums_dict = {}``` ➡️ **n**<br>
    ```for n in nums``` ➡️  **1**<br>
    ```nums_dict[n] = 0``` ➡️  **1**<br>
    <br> ➡️ n + 1 + 1 ➡️ n + 2
<br>

4. Drop all constants and find the dominant term.<br>
➡️ n + 2 ➡️ n + 1 ➡️ n
<br>

5. Match this to the most relevant complexity.<br>
    1 ➡️ **O(n) - Linear Space**<br>
    <br>*The algorithm will grow in space directly proportional to the input size. The complexity increases at the same rate that the input increases.*
<br>