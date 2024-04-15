# Given an array of characters where each character represents a fruit tree, 
# you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, i.e., 
# you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

 

def totalFruit(fruits) -> int:
        max_length, win_start = 0, 0
        fruit_freq = {}
        
        for win_end in range(len(fruits)):
            fruit_left = fruits[win_end]
            if fruit_left not in fruit_freq:
                fruit_freq[fruit_left] = 0
            fruit_freq[fruit_left] += 1
            
            while len(fruit_freq) > 2:
                fruit_right = fruits[win_start]
                fruit_freq[fruit_right] -= 1
                if fruit_freq[fruit_right] == 0:
                    del fruit_freq[fruit_right]
                win_start += 1
            
            max_length = max(max_length, win_end - win_start + 1)
        return max_length

fruits = ['A', 'B', 'C', 'B', 'B', 'C']
print("Original Array", fruits)
print("The maximum number of fruits you can pick : ", totalFruit(fruits))