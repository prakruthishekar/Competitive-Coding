# Given n pairs of parentheses, write a function to generate all 
# combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]


def generateParenthesis(n: int):
	def dfs(left, right, s):
		if len(s) == n * 2:
			res.append(s)
			return 

		if left < n:
			dfs(left + 1, right, s + '(')

		if right < left:
			dfs(left, right + 1, s + ')')

	res = []
	dfs(0, 0, '')
	return res

print(generateParenthesis(2))




					# 			   	(0, 0, '')
					# 			 	    |	
					# 				(1, 0, '(')  
					# 			   /           \
					# 		(2, 0, '((')      (1, 1, '()')
					# 		   /                 \
					# 	(2, 1, '(()')           (2, 1, '()(')
					# 	   /                       \
					# (2, 2, '(())')                (2, 2, '()()')
					# 	      |	                             |
					# res.append('(())')             res.append('()()')
   