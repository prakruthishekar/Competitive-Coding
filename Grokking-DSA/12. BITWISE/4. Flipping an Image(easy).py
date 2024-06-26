# Given a binary matrix representing an image, we want to flip the image horizontally, 
# then invert it.

# To flip an image horizontally means that each row of the image is reversed. 
# For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
# For example, inverting [1, 1, 0] results in [0, 0, 1].

# Example 1:

# Input: [
#   [1,0,1],
#   [1,1,1],
#   [0,1,1]
# ]
# Output: [
#   [0,1,0],
#   [0,0,0],
#   [0,0,1]
# ]
# Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. 
# Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

# Example 2:

# Input: [
#   [1,1,0,0],
#   [1,0,0,1],
#   [0,1,1,1], 
#   [1,0,1,0]
# ]
# Output: [
#   [1,1,0,0],
#   [0,1,1,0],
#   [0,0,0,1],
#   [1,0,1,0]
# ]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. 
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

def flip_an_inverted_image(matrix):

    lengthMatrix = len(matrix)

    for row in matrix:
        for i in range((lengthMatrix + 1) // 2):
            row[i] = row[lengthMatrix - i - 1] ^ 1
            row[lengthMatrix -i - 1] = row[i] ^ 1  

    return matrix




# def flip_an_inverted_image(matrix):
#   for row in matrix:
#             left = 0
#             right = len(row)-1
#             while(left <= right):
#                 if(left == right):
#                     row[left] = row[left] ^ 1
#                     break
#                 temp = row[left]
#                 row[left] = (row[right]) ^ 1
#                 row[right] = temp ^ 1

#                 left += 1
#                 right -= 1
                
#         return matrix 

print(flip_an_inverted_image([
  [1,1,0,0],
  [1,0,0,1],
  [0,1,1,1], 
  [1,0,1,0]
]))
print(flip_an_inverted_image([
  [1,0,1],
  [1,1,1],
  [0,1,1]
]))