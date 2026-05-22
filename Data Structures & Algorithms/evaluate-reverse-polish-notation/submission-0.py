class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)  # truncates toward zero
        }
        
        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                stack.append(operators[token](a, b))
            else:
                stack.append(int(token))
        
        return stack[0]      