# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a 
# single character.

# Example 3:

# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".


def compress(chars):
    # Pointer to read the characters
    read = 0
    # Pointer to write the compressed characters and counts
    write = 0

    while read < len(chars):
        char = chars[read]
        count = 0
        # Count consecutive occurrences of the character
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1

        # Write the character to chars
        chars[write] = char
        write += 1

        # If there's more than one occurrence, write the count to chars
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a"]))
