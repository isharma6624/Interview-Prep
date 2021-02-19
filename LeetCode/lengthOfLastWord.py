class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        i = 0 
        s = s.rstrip()
        for c in range(len(s)-1,-1,-1):
            if str(s[c]) != str(" "):
                i += 1
            else:
                break
        
        return i
