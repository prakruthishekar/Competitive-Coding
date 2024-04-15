def longest_no_repeat_substring(s) -> int:
        char_freq = {}
        left = right = 0
        res = 0
        while right < len(s):
            r = s[right]
            if(r not in char_freq):
                char_freq[r] = 0
            char_freq[r] += 1
            while char_freq[r] > 1:
                l = s[left]
                char_freq[l] -= 1
                # if(char_freq[r] == 1):
                #     del char_freq[r]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res  

print("araaci : ", longest_no_repeat_substring("araaci"))
print("abcabcbb : ", longest_no_repeat_substring("abcabcbb"))
print("bbbbb : ", longest_no_repeat_substring("bbbbb"))
print("pwwkew : ", longest_no_repeat_substring("pwwkew"))
print("ohomm : ", longest_no_repeat_substring("ohomm"))