class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ans = list()
        nums.sort()
        
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1,len(nums)-2):
                if j >i + 1 and nums[j] == nums[j-1]:
                    continue
                    
                low,high = j + 1, len(nums) - 1
                
                while low < high:
                    
                    if nums[i] + nums[j] + nums[low] + nums[high] == target:
                        ans.append([nums[i],nums[j],nums[low],nums[high]])
                        
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1

                        while low <high and nums[high] == nums[high-1]:
                            high -= 1
                        
                        low += 1
                        high -= 1
                        
                        
                    elif nums[i] + nums[j] + nums[low] + nums[high] > target:
                        high -= 1
                    
                    else:
                        low += 1
            
            
        
        return ans

#run time = O(n^3)
                    
