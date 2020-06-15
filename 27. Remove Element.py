class Solution:
    def removeElement(self, nums, val):
        
        while nums.count(val) != 0:
            for num in nums[0:]:
                if val == num:
                    nums.remove(val)
            
            lenght = len(nums) 
            return lenght
    

s = Solution()
p = s.removeElement([0,1,2,2,3,0,4,2], 2)
print(p)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = 0
#         length = len(nums)
#         while i < length :
#             if nums[i] == val:
#                 del nums[i]
#                 length -= 1
#             else :
#                 i += 1
        
#         return length
                
        