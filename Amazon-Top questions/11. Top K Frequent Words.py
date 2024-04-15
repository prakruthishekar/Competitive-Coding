# Given an array of strings words and an integer k, return the k most frequent strings.

# Return the answer sorted by the frequency from highest to lowest. 
# Sort the words with the same frequency by their lexicographical order.

 

# Example 1:

# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:

# Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words, 
# with the number of occurrence being 4, 3, 2 and 1 respectively.


def topKFrequent(words, k: int):
        dict = {}
        for x in words:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1
  
        res = sorted(dict, key=lambda x: (-dict[x], x))
        return res[:k]
# -dict[x] is used as the primary sorting criterion. 
# It sorts the keys in descending order based on the corresponding values
# in the dictionary. The negative sign - is used to reverse the 
# sorting order.


# x is used as the secondary sorting criterion. 
# It sorts the keys in ascending order lexicographically when the 
# values are equal.

        

print(topKFrequent(["i","love","leetcode","i","love","coding"],2))        