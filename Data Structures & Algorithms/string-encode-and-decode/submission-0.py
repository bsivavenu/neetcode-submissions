class Solution:

    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = []
        for s in strs:
            # Prefix each string with 'length#'
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length of the string
            length = int(s[i:j])
            
            # Extract the exact string content based on the length
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            
            # Move index to the start of the next length-prefix
            i = end
            
        return decoded