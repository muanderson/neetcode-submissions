class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)
        
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # Find the delimiter #
            j = i
            while s[j] != '#':
                j += 1
            
            # Get the length of the next string
            length = int(s[i:j])
            
            # Get the actual string using the length
            # Start after the #, read 'length' characters
            result.append(s[j + 1:j + 1 + length])
            
            # Move pointer to start of next length#string
            i = j + 1 + length
            
        return result

            

