# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. 
# If there are multiple longest happy strings, return any of them. If there is 
# no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.


import heapq


def longestDiverseString(a: int, b: int, c: int) -> str:
    res , maxheap = "", []
    for count, char in [(-a,"a"),(-b,"b"), (-c,"c")]:
        if count != 0:
            heapq.heappush(maxheap, (count, char))

    while maxheap:
        count, char = heapq.heappop(maxheap)
        if len(res) > 1 and res[-1] == res[-2] == char:
            if not maxheap:
                break
            count2, char2 = heapq.heappop(maxheap)
            res += char2
            count2 += 1
            if count2:
                heapq.heappush(maxheap,(count2, char2))

        else:
            res += char
            count += 1
        if count: 
            heapq.heappush(maxheap, (count, char))

    return res

print(longestDiverseString(1,1,7))
print(longestDiverseString(7,1,0))
