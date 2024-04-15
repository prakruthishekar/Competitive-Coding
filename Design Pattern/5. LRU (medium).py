class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity   

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        val = self.dict.pop(key)  #Remove it first before inserting it at the end again
        self.dict[key] = val   
        return val        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:    
            self.dict.pop(key)
        else:
            if len(self.dict) == self.capacity:
                del self.dict[next(iter(self.dict))]    
        self.dict[key] = value


lRUCache = LRUCache(2)
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.put(3, 4); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4
        

from collections import OrderedDict

# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Convert the dictionary to an OrderedDict
ordered_dict = OrderedDict(my_dict)

# Pop the first item from the OrderedDict
if ordered_dict:  # Ensure the OrderedDict is not empty
    ordered_dict.popitem(last=False)

# Convert the OrderedDict back to a regular dictionary if needed
my_dict_updated = dict(ordered_dict)

print(my_dict)

