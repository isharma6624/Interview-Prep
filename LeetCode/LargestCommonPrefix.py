class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
    
        common = ""
        minLength = min(strs,key = len)
        if minLength == 0:
            return common
        flag = True
        for i in range (len(minLength)):
            prev = minLength[i]
            
            for item in range(len(strs)):
                if(strs[item][i] != prev):
                    flag = False
                    
            if flag == True:
                common += minLength[i]
                
        return common
