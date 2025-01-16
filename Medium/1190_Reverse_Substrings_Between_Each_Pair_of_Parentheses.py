class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                temp = ""
                while stack and stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                stack.append(temp[::-1])
            else:
                stack.append(char)
        return "".join(stack)
