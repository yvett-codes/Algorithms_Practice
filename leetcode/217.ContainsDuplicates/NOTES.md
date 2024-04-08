# 217.Contains Duplicates

## Approach
Used a hash table to check if there was an already existing integer. If the integer did not exist, we create a key for *n*. If the integer already existed, we returned **True**.

## Time Complexity
O(n); We only scanned through the list of inputs once and we had to perform the same operations for each item in the list.


## Space complexity:
O(n); We sacrificed memory by creating a hash table, which is dependent on the size of the input array, which is *n*.