class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s)<2:
            return False
        
        mapping = {
            "(" : ")",
            "{": "}",
            "[":"]"
        }
        
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)
            
            else:
                if not stack:
                    return False
                
                elif mapping[stack.pop()] != c:
                    return False
                             
        return not stack
