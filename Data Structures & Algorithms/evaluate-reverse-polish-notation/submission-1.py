class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the operands in reverse order
                b = stack.pop()
                a = stack.pop()
                
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # int() handles division truncation toward zero automatically
                    stack.append(int(a / b))
            else:
                # Token is an integer, push it to stack
                stack.append(int(token))
                
        return stack[0]