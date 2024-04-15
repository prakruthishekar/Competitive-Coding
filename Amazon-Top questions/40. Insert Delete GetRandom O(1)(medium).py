# Implement the RandomizedSet class:

# RandomizedSet() Initializes the RandomizedSet object.

# bool insert(int val) Inserts an item val into the set if not present.
# Returns true if the item was not present, false otherwise.

# bool remove(int val) Removes an item val from the set if present. 
# Returns true if the item was present, false otherwise.

# int getRandom() Returns a random element from the current 
# set of elements (it's guaranteed that at least one element
#  exists when this method is called). Each element must have the same 
# probability of being returned.

# You must implement the functions of the class such that each 
# function works in average O(1) time complexity.




import random

class RandomizedSet:
    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        index = self.indices[val]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.indices[last_val] = index
        self.values.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)



# To implement the RandomizedSet class with the desired time complexity,
#  you can use a combination of a dictionary and an array. The dictionary
#  will provide O(1) average time complexity for insertion and removal 
#  operations, while the array will allow for O(1) time complexity for 
#  the getRandom operation. Here's the Python implementation:

randomizedSet = RandomizedSet()
print(randomizedSet.insert(1)) # Inserts 1 to the set. Returns true as 1 was inserted successfully.
print(randomizedSet.remove(2)) # Returns false as 2 does not exist in the set.
print(randomizedSet.insert(2)) # Inserts 2 to the set, returns true. Set now contains [1,2].
print(randomizedSet.getRandom()) # getRandom() should return either 1 or 2 randomly.
print(randomizedSet.remove(1)) # Removes 1 from the set, returns true. Set now contains [2].
print(randomizedSet.insert(2)) # 2 was already in the set, so return false.
print(randomizedSet.getRandom()) # Since 2 is the only number in the set, getRandom() will always return 2.