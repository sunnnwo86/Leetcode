# class Solution:
#     def maxSubArray(self, nums):


#         nums.sort()
#         print(nums)
#         b = []
#         b = nums[:-5:-1]

#         return sum(b),print(b)
class Solution:
    # @param A, a list of integers
    # @return an integer
    # 6:57
    def maxSubArray(self, A):
        if not A:
            return 0

        curSum = maxSum = A[0]
        
        for num in A[1:]:
            # 1 -2 4 3 5 6 1 5
            curSum = max(num, curSum + num)
           
            maxSum = max(maxSum, curSum)
            print(maxSum)
        return maxSum   
s = Solution()
p = s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(p)


