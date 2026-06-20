class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            # A collision only occurs if the stack top is moving RIGHT (+) 
            # and the current asteroid is moving LEFT (-)
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:
                    # The right-moving asteroid is smaller; it explodes.
                    # Pop it and check the next one in the stack.
                    stack.pop()
                    continue
                elif stack[-1] == -ast:
                    # Both are the same size; both explode.
                    stack.pop()
                
                # If stack[-1] > -ast, the current asteroid explodes.
                # In both equal and smaller cases, the current asteroid is destroyed.
                break
            else:
                # This executes only if the while loop condition becomes False 
                # (i.e., no collision occurred, or it destroyed all right-moving asteroids)
                stack.append(ast)
                
        return stack