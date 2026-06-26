class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # Split by slashes to isolate directory names and commands
        components = path.split('/')
        
        for component in components:
            # If it's an empty string or a single dot, stay in current directory
            if component == "" or component == ".":
                continue
            # If it's a double dot, move up to the parent directory
            elif component == "..":
                if stack:
                    stack.pop()
            # It's a valid directory or file name (e.g., "..." is valid)
            else:
                stack.append(component)
                
        # Join components with a single slash and prepend the root slash
        return "/" + "/".join(stack)