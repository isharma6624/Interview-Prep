class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        result = []
        if digits =="":
            return []

        phoneDict = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",

                }

        self.letterCombinationshelper(result, digits, "", 0, phoneDict)
        return result


    def letterCombinationshelper(self,result,digits, current,index,phoneDict):
        if index == len(digits):
            result.append(current)
            return result


        letters = phoneDict[str(digits[index])]
        for item in letters:
            self.letterCombinationshelper(result,digits, current + item,index + 1,phoneDict):
