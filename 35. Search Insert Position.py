class Solution:
    def searchInsert(self, nums, target):
        
        if min(nums) >= target:
            nums.insert(0, target)
            print(nums.index(target))
            
        
        elif max(nums) < target:
            nums.append(target)    
            
        
        
        count = 0
        
        while count < len(nums):
            
            # if nums[count] == target:
            #     nums.insert(count, target)
            
          
            
            if  nums[count] < target <= nums[count + 1]:  
                nums.insert(count+1, target)
                # print(nums)
                counter = nums.index(target)
                # print(counter)
                return counter
            count += 1

s = Solution()

a = s.searchInsert([1,2,3,4,5], 0)
print(a)