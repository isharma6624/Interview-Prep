class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if nums == []:
            return 0
        
        ans = -1
        for i in range(len(nums)):
            if val - nums[i] != 0:
                ans += 1
                nums[ans] = nums[i]
            
        return ans + 1
