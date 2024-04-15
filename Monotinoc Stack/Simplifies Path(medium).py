# Example 1:

# Input: path = "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory name.
# Example 2:

# Input: path = "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, 
# as the root level is the highest level you can go.


def simplifyPath(path: str) -> str:
    stack = []
    for str in path:
        if str == ".":
            continue
        if stack and str == "/" and stack[-1] == "/":
                continue
        stack.append(str)
    if len(stack) > 1 and stack[-1] == "/":
         stack.pop()

    return "".join(stack)

print(simplifyPath("/home/"))
print(simplifyPath("/../"))
