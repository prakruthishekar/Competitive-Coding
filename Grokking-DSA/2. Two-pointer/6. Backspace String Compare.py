# # With Deque: (six lines)

# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#         a, A = [collections.deque(), collections.deque()], [S,T]
#         for i in range(2):
#             for j in A[i]:
#                 if j != '#': a[i].append(j)
#                 elif a[i]: a[i].pop()
#         return a[0] == a[1]



# # Without Deque: (four lines)

# class Solution:
#     def backspaceCompare(self, S: str, T: str) -> bool:
#     	s, t = [], []
#     	for i in S: s = s + [i] if i != '#' else s[:-1]
#     	for i in T: t = t + [i] if i != '#' else t[:-1]
#     	return s == t








# class Solution:
#     def backspaceCompare(self, s, t):
        
#         stack1=[]
#         stack2=[]
        
#         for char in s:
#             if(char=="#"):
#                 if stack1:
#                     stack1.pop()
#             else:
#                 stack1.append(char)
                
#         for char in t:
#             if(char=="#"):
#                 if stack2:
#                     stack2.pop()
#             else:
#                 stack2.append(char)

#         if(stack1==stack2):
#             return True
#         else:
#             return False




# # Two-Pointer: (eight lines)

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_ptr = len(s) - 1
        t_ptr = len(t) - 1
        s_skip = 0
        t_skip = 0

        while s_ptr >= 0 or t_ptr >= 0:
            while s_ptr >= 0:
                if s[s_ptr] == '#':
                    s_skip += 1
                    s_ptr -= 1
                elif s_skip > 0:
                    s_skip -= 1
                    s_ptr -= 1
                else:
                    break

            while t_ptr >= 0:
                if t[t_ptr] == '#':
                    t_skip += 1
                    t_ptr -= 1
                elif t_skip > 0:
                    t_skip -= 1
                    t_ptr -= 1
                else:
                    break

            if s_ptr >= 0 and t_ptr >= 0 and s[s_ptr] != t[t_ptr]:
                return False

            if (s_ptr >= 0) != (t_ptr >= 0):
                return False

            s_ptr -= 1
            t_ptr -= 1

        return True


S = "y#fo##f"

T = "y#f#o##f"
classObject = Solution()
print(classObject.backspaceCompare(S,T))