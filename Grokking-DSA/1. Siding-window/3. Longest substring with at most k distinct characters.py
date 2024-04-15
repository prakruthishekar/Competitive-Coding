# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".
# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".
# Example 3:

# Input: String="cbbebi", K=3
# Output: 5
# Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

def longSubtringKDistinct(str, k) -> int:
        max_length, win_start = 0, 0
        char_freq = {}
        
        for win_end in range(len(str)):
            char_left = str[win_end]
            if char_left not in char_freq:
                char_freq[char_left] = 0
            char_freq[char_left] += 1  

            while(len(char_freq) > k ):
                char_present = str[win_start]
                char_freq[char_present] -= 1
                if(char_freq[char_present] == 0):
                    del char_freq[char_present]
                win_start += 1 

            max_length = max(max_length, win_end - win_start + 1)
        return max_length

print("araaci : ", longSubtringKDistinct("araaci", 2))
print("araaci : ", longSubtringKDistinct("araaci",1))
print("cbbebi : ", longSubtringKDistinct("cbbebi", 3))

#Time Complexity : O(n)    