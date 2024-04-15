# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the 
# value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called 
# previously, with timestamp_prev <= timestamp. If there are multiple such values,
# it returns the value associated with the largest timestamp_prev. If there are no values, 
# it returns "".


# How to know when to use binary search -> Constraints
# O(logN)


# class TimeMap:
#   # bin search soln
#   def __init__(self):
#     self.store = {} 
#     # hashmap, key = string, val = [list of [val, timestamp]] {foo -> [bar, 1]}

#   def set(self, key: str, value: str, timestamp: int) -> None:
#     if key not in self.store:
#       # insert
#       self.store[key] = [] # set to empty list.
#     self.store[key].append([value, timestamp]) # append val & times

#   def get(self, key: str, timestamp: int) -> str:
#     res = "" # if not exist just return empty
#     values = self.store.get(key, []) # find match it'll return that list if doesn't then returns empty list (by default) [values is a list]
    
#     # binary  search
#     low, high = 0, len(values) - 1
#     while low <= high:
#       mid = (low + high) // 2
#       # values[mid] will be a pair of values and timestamps
#       # we only need to check timestamps (which is in incr order) hence values[mid][1]
#       if values[mid][1] <= timestamp:
#         # if equal or less than timestamp -> ans found
#         res = values[mid][0] # closest we've seen so far -> store in ans
#         low = mid + 1 # check for closer values
#       else:
#         # not allowed (acc to question)
#         high = mid - 1 # don't assign any result here as this is an invalid val
#     return res
  




import bisect
import collections


class TimeMap:
    def __init__(self):
        self.meta = collections.defaultdict(list)
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.meta[key].append(timestamp)
        self.data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
# bisect.bisect does not sort the list. Instead, it assumes 
# the list is already sorted and finds the position where a 
# given element should be inserted to keep it sorted. The 
# function returns the index where the element should be 
# inserted. If the element is already present in the list, 
# the returned index will be after all occurrences of the 
# element in the list.
        idx = bisect.bisect(self.meta[key], timestamp)
        if idx == 0:
            return ''
        return self.data[key][idx - 1]


timeMap = TimeMap()
timeMap.set("foo", "bar", 1) # store the key "foo" and value "bar" along with timestamp = 1.
print(timeMap.get("foo", 1));        # return "bar"
print(timeMap.get("foo", 3));        # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); # store the key "foo" and value "bar2" along with timestamp = 4.
print(timeMap.get("foo", 4));         # return "bar2"
print(timeMap.get("foo", 5));         # return "bar2" 