# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]

# class Solution:
#     def twoSum(self, nums, target):
#         nums = [2, 7, 11, 15]
#         for num in nums:
#             print(num)
            
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            print("nnnnnnnnnnn",n)
            if n not in h:
                h[num] = i
                print(h)
                print("iIIIIIIIIIII",i)
            else:
                return [h[n], i]

c = Solution()
d=c.twoSum([11,23,1,2,3,4,5,6,1,2,77,5,4,33,2,4,5,6,1,2,3,4,6,2,3,4],110)
print(d)