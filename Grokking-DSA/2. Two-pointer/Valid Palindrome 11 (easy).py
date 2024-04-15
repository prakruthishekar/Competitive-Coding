def validPalindrome( s: str) -> bool:
        right = len(s) - 1
        left = 0
        flag = 0
        while right > left:
            if flag > 1:
                return False

            if (s[left] != s[right]):
                flag += 1
                right -= 1
                left += 1
            else:
                right -= 1
                left += 1
                
        if flag > 1 and right == left:
            return False
        else: 
            return True
        
print(validPalindrome("deeee"))