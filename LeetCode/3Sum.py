class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = list()

        for i in range(len(nums)-2):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]) 

                low, high = i + 1, len(nums)-1

                while low < high:
                    if(nums[low] + nums[high] + nums[i] == 0):
                        ans.append([nums[i],nums[j],nums[k]])

                        while(low < high and nums[low]==nums[low +1]):
                            low += 1

                        
                        while(low < high and nums[high]==nums[high - 1]):
                            high -= 1


                        low += 1
                        high -= 1


                    elif(nums[low] + nums[high] > 0-nums[i]):
                        high -= 1

                    else:
                        low += 1


        return ans
