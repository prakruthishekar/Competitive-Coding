# You are keeping the scores for a baseball game with strange rules. 
# At the beginning of the game, you start with an empty record.

# You are given a list of strings operations, where operations[i] 
# is the ith operation you must apply to the record 
# and is one of the following:

# An integer x.
# Record a new score of x.
# '+'.
# Record a new score that is the sum of the previous two scores.
# 'D'.
# Record a new score that is the double of the previous score.
# 'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.

# The test cases are generated such that the answer and all 
# intermediate calculations fit in a 32-bit integer and that all operations are valid.


def calPoints(operations) -> int:
        stack = []
        for num in operations:
            if num == 'C': stack.pop()
            elif num == 'D': stack.append(2 * stack[-1])
            elif num == '+': stack.append(stack[-1] + stack[-2])
            else: stack.append(int(num))
        return sum(stack)




# The time and space complexity of the calPoints function can be analyzed as follows:

# Let n be the number of elements in the operations list.
# The function iterates over each element in the operations list exactly once.
# For each element, it performs a constant number of operations (pushing, popping, or performing arithmetic operations) on the stack data structure.
# Therefore, the time complexity of the function is O(n).

# Regarding space complexity:

# The function uses a stack data structure to store intermediate results.
# The size of the stack is determined by the number of valid operations encountered in the operations list.
# In the worst case, all elements in the operations list are valid operations, so the size of the stack can grow up to n.
# Therefore, the space complexity of the function is O(n) since it requires additional space proportional to the input size.
# In summary, the time complexity of the calPoints function is O(n), and the space complexity is also O(n)


def calPoints(operations) -> int:
    i = j = 0
    while j < len(operations):
        if operations[j] == "C":
            i -= 2
        elif operations[j] == "D":
            operations[i] = int(operations[i-1])*2
        elif operations[j] == "+":
            operations[i] = int(operations[i-1]) + int(operations[i-2])
        else:
            operations[i] = int(operations[j])
        i += 1
        j += 1
    return sum(operations[:i])

# Let n be the number of elements in the operations list.
# The function uses two pointers, i and j, to traverse the operations list. It updates these pointers in a single pass through the list.
# For each element, the function performs a constant number of operations (assignment, arithmetic operations, type conversion) and updates the values in the operations list in-place.
# Therefore, the time complexity of the function is O(n).
# Regarding space complexity:

# The function operates directly on the operations list without using any additional data structures.
# It uses a constant amount of extra space for the two pointers i and j.
# Therefore, the space complexity of the function is O(1) (constant space).
# In summary, the time complexity of the modified calPoints function is O(n), and the space complexity is O(1).

print(calPoints(["5","2","C","D","+"]))