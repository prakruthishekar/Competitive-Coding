# Problem Statement #
# Any number will be called a happy number if, after repeatedly replacing it with a number equal 
# to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy)
#  numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does 
#  not include ‘1’.



#  Example 1:

# Input: 23   
# Output: true (23 is a happy number)  
# Explanations: Here are the steps to find out that 23 is a happy number:
# 2^2 + 3 ^22
# ​2
# ​​ +3
# ​2
# ​​  = 4 + 9 = 13
# 1^2 + 3^21
# ​2
# ​​ +3
# ​2
# ​​  = 1 + 9 = 10
# 1^2 + 0^21
# ​2
# ​​ +0
# ​2
# ​​  = 1 + 0 = 1



# List comprehension approach along with set()
# def isHappy(n):
#         num_set = set()
#         while n != 1:
#             n = sum([int(d) ** 2 for d in str(n)])
#             if n in num_set:
#                 return False
#             else:
#                 num_set.add(n)
#         return True

def isHappy(num):
    slow, fast = num, num
    while True:
        slow = find_square_sum(slow) # move one step
        fast = find_square_sum(find_square_sum(fast)) # move two steps
        if(slow == fast): # Found cycle
            break
    return slow == 1 # see if the cycle is stuck at 1


def find_square_sum(num):
    sum = 0
    while(num > 0):
        digit = num % 10
        sum += digit * digit
        num //= 10
    return sum      

def main():
    print(isHappy(23))
    print(isHappy(12))


main()    