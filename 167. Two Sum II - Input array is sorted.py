class Solution:
    def twoSum(self, nums, target):

        hass = {}
        result = []
        
        
        for i , num in enumerate(nums):
            
            if hass.get(num) is None:
                hass[target - num] = i
            else:
                result = [hass[num]+1, i+1]
        # print( i+1) 
        # print(result)  
        return result
    
s = Solution()
t = s.twoSum([7,11,15,2],9)
print(t)