# class Solution:
#     def singleNumber(self, nums):
#         counter = {}
#         for num in nums:
#            if num in counter:
#                counter[num] += 1
#            else:
#                counter[num] = 1
#         counter.values()
#         for my_key, my_value in counter.items():
            
#             if my_value == 1:
                
#                 return my_key

        
        
        

# for my_key, my_value in pawo.items():
    
#       if my_value == search_value:

#             print(my_key)

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)
    
s = Solution()
a = s.singleNumber([111,1,1,1,1,1,1,1])
print(a)
