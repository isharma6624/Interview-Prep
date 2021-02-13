class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
#         [-4,-1,1,2]
        nums.sort()
        ans = float('inf')
        for i in range(len(nums)-2):
            
            low, high = i+1, len(nums)-1

            while(low < high):
                if nums[i] + nums[low] + nums[high] == target:
                    return target
                else:
                    sums = nums[i] + nums[low] + nums[high]
                    if abs(ans - target) > abs(sums - target):
                        ans = sums
                    
                    if nums[i] + nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1
        return ans
