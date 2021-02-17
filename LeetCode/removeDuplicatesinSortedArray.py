class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        ans = 0
        for i in range(1,len(nums)):
            while(nums[ans] != nums[i]):
                ans += 1
                nums[ans] = nums[i]
            
            
        
        return ans +1
