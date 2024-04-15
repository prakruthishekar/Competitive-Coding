#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        MAPPING = {
                "1": 1,
                "2": 2,
                "3": 3,
                "4": 4,
                "5": 5,
                "6": 6,
                "7": 7,
                "8": 8,
                "9": 9,
                "0": 0,
            }

        MAX_INT = 2**31-1
        MIN_INT = -(2**31)

        def limit(x: int) -> int:
            if x > MAX_INT:
                return MAX_INT
            if x < MIN_INT:
                return MIN_INT
            return x

        s = s.lstrip(' ')
        if not s:
            return 0
        
        sign = -1 if s[0] == "-" else 1
        if sign != 1 or s[0] == "+":
            s = s[1:]
            
        res = 0
        for c in s:
            if c not in MAPPING:
                return limit(res * sign)
            
            res *= 10
            res += MAPPING[c]
            
        return limit(res * sign)