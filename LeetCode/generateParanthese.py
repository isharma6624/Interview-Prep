# using backtracking algo
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.backtrack(output,"",0,0,n)
        return output
    
    def backtrack(self,output,current,openb,close,n):
        if len(current) == 2*n:
            output.append(current)
            return
        
        if (openb < n):
            self.backtrack(output,current + "(",openb + 1 ,close,n)
        if (close < openb):
            self.backtrack(output, current + ")",openb,close + 1,n)
