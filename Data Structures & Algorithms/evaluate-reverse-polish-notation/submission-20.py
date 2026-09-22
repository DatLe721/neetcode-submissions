class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            
            if token == '+':
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(s1+s2)
            elif token == '-':
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(s1-s2)
            elif token == '/':
                s2 = stack.pop()
                s1 = stack.pop()
                stack.append(int(s1/s2))
            elif token == '*':
                s1 = stack.pop()
                s2 = stack.pop()
                stack.append(s1*s2)
            else:
                stack.append(int(token))
        return int(stack[-1])