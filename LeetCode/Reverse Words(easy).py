# Given a string s, reverse the order of characters in each word 
# within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"


def reverseWords(s):
    res = ''
    l, r = 0, 0
    while r < len(s):
        if s[r] != ' ':
            r += 1
        elif s[r] == ' ':
            res += s[l:r + 1][::-1]
            r += 1
            l = r
    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]

# def reverseWords(s: str) -> str:
#         split_list = s.split(" ")
#         split_list = [i[::-1] for i in split_list]
#         return " ".join(split_list)


print(reverseWords("Let's take LeetCode contest"))        