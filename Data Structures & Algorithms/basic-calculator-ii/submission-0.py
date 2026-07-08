class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        current_number = 0
        last_operator = '+'
        operators = {'+', '-', '*', '/'}
        
        for i, char in enumerate(s):
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            
            # If the character is an operator or we reached the end of the string
            if char in operators or i == len(s) - 1:
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif last_operator == '/':
                    # int() division in Python truncates towards zero
                    stack.append(int(stack.pop() / current_number))
                
                last_operator = char
                current_number = 0
                
        return sum(stack)