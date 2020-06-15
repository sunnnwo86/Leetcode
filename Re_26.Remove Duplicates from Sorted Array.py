class Solution:
    def removeDuplicates(self, nums):
        nums[:] = set(nums)
        return len(nums)
    
#         nums = [0,0,1,1,1,2,2,3,3,4]
#         i = 0
#         while i < 1000:
            
#             a = min(nums)
#             b = max(nums)
#             c = range(a,b)
#             for d in c:
#                 print(d)
#                 nums.count(d) 
#                 if nums.count(d) >= 2:

#                     for b in range(nums.count(d)-1):
#                         nums.remove(d)
#             i += 1
#         print(nums)

s = Solution()
print(s.removeDuplicates([-1,-1,-1,1,2,3,4,55,5,5,5,5]))        
# #         # q = min(nums)
#         # w = max(nums)
        # e = range(q,w)
        
        # i = q
        # while  q <= i <=w:
           
            
        #     if nums.count(i) != 1:
                
        #         for b in range(nums.count(i)-1):
        #             nums.remove(i)
                
        #             i = q + 1
        # # return len(nums)
        # while True:
        #     for a in nums:
        #         b = nums.count(a)
        #         x = b-1
        #         if nums.count(a) != x:
        #             b = nums.count(a)
        #             # print(b)
        #             # x = b-1
        #             print("x:",x)
        #             nums.remove(a)
        #             print(nums)
        #             # print(nums)
        #         elif nums.count(a) == x:
        #             nums.append
        #             return nums
        #             # return len(nums), nums
                # elif nums.count(a) == 1:
                #     return len(nums),nums
      
        # for a in nums:
        #     b = nums.count(a)
        #     x = b-1
            
        #     print("1x:",x)
        #     while True:

        #         if nums.count(a) != 1:
        #             b = nums.count(a)
        #             # print(b)
        #             x = b-1
        #             print("x:",x)
        #             nums.remove(a)
        #         elif nums.count(a) == 1:
        #             return len(nums), nums   
                
                
                    # while x == 1:
                    #     # nums.remove(a)

                    #     if nums.remove(a) == 1:
                    #         return print(nums)

                    #     print(nums)

                    
       
                
                               
# s = Solution()
# # print(s.removeDuplicates([1,1,1,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,6]))

# # a = [1,2,3,4,4,4,4,12,3,4,5,5,6,1,2,3,1,23,1,24,65,674,56,12,12,3]

# # i = 0
# # while i < 1000:
# #     i += 1
# #     a.count(i) 
# #     if a.count(i) >= 2:
        
# #         for b in range(a.count(i)-1):
# #             a.remove(i)
# # print(a)

# class Solution:
#     def removeDuplicates(self, nums):
#         dic_a = {}
        
#         for num in nums:
            
#             if num in dic_a:
#                 dic_a[num] += 1
                
#             else:
#                 dic_a[num] = 1
        
#         nums = list(dic_a.keys())
#         print(nums)
#         d = len(nums)
#         return nums, d
       

# s = Solution()
# print(s.removeDuplicates([1,1,2]))               
                
            
          
  