class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort both arrays to apply the greedy approach
        g.sort()
        s.sort()
        
        child_ptr = 0
        cookie_ptr = 0
        
        # Iterate through both arrays until we run out of children or cookies
        while child_ptr < len(g) and cookie_ptr < len(s):
            # If the cookie can satisfy the child, move to the next child
            if s[cookie_ptr] >= g[child_ptr]:
                child_ptr += 1
            # Always move to the next cookie
            cookie_ptr += 1
            
        # The index of child_ptr represents the total number of content children
        return child_ptr