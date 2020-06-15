# # class Solution:
# #     def two_Sum(self, nums, target):
# #         compliments = {}
# #         result = []
        
# #         for index , num in enumerate(nums):
# #             if compliments.get(num) is None:
# #                 compliments[target - num] = index
# #             else:
# #                 result = [compliments[num], index]
# #         return result

# # l = Solution()

# # print(l.two_Sum([1,5,2,3,6,7,11,15], 22))
# # """
# # # compliments = {
# # #     21 : 0
# # #     17 : 1
# # #     20 : 2
# # #     19 : 3
# # #     16 : 4
# # #     15 : 5
# # #     11 : 6
# #     7  : 7
    
# # }
# # """


# # class Solution:
# #     def twoSum(self, nums, target):
# #         hass = {}
# #         result = []
        
        
# #         for i , num in enumerate(nums):
            
# #             if hass.get(num) is None:
# #                 hass[target - num] = i
# # #             else:
# # #                 result = [hass[num], i]
# # #         return result


# # a = [1,1,1,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,6]

# # i = 0
# # while i < 1000:
# #     i += 1
    
# #     if a.count(i) >= 2:
        
# #         for b in range(a.count(i)-1):
# #             a.remove(i)
# # print(a)

# symbol = {
#           "I" : 1,
#           "V" : 5,
#           "x" : 10,
#           "L" : 50,
#           "C" : 100,
#           "D" : 500,
#           "M" : 1000,
#           "IX" : 9,
#           "IV" : 5,
#           "XL" : 40,
#           "XC" : 90,
#           "CD" : 400,
#           "CM" : 900
#               }

# s = "qwerasdzxc"
# print(s[3:3+2])

# # i =+ symbol.get("IX")
# # i = i + symbol.get("I")
# # i = i + symbol.get("D")
# # print(type(i))
# # print(i)

# # a = "assdda"
# # b=2
# # print(a[b],a[b-1])
    
# # class Solution(object):
# #     def romanToInt(self, s):
# #       """
# #       :type s: str
# #       :rtype: int
# #       """
# #     roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
# #     i = 0
# #     num = 0
# #     while i < len(s):
# #         if i+1<len(s) and s[i:i+2] in roman:
# #             num+=roman[s[i:i+2]]
# #             i+=2
# #         else:
# #             #print(i)
# #             num+=roman[s[i]]
# #             i+=1
# #         return  num
# # ob1 = Solution()
# # print(ob1.romanToInt("III"))
# # print(ob1.romanToInt("CDXLIII"))

# python = "Python is Amazing"
# print(python[0].isupper())
# print(python.replace("Python", "java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("java")) #JAVA가 없으면 -1 출력해줌.


# url = "http://naver.com"
# my_str = url.replace("http://", "")
# print(my_str)
# my_str = my_str[:my_str.index(".")] # "." 앞까지만 출력 my_str이라는 문자열 안에서 처음 나오는 .의 위치까지 잘라라.
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{} 의 비밀번호는 {} 입니다.".format(url, password))

# java = {"a", "b", "c"}
# java =list(java)

# print(java,type(java))
# from random import *
# a = range(10)
# print(a)
# b = list(a)
# print(b)
# shuffle(b)
# print(b)
# winners = sample(b,4)
# print(winners[0])
# print(winners[1:])
# print(type(winners))

# bb = 2
# aa = [1,2,3,4,5,6,2]
# aaa = [100,111,1111]
# aaa.insert(1,100)
# aaa.index(100)
# print(aaa.index(100))
# # print(max(aaa))
# # print(aaa.count(1))

# # for a1 in aa:
# #     if bb == a1:
# #         aa.remove(bb)
# # length=len(aa)
# # print(length)
# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         globalMax = nums[0]
        
#         curr = nums[0]
        
#         for i in range(1, len(nums)):
            
#             curr = max(nums[i], nums[i]+curr)
            
#             globalMax = max(globalMax, curr)
            
#         return globalMax

# s = Solution()
# aaaa=s.maxSubArray([-1,2,3,-4,5,6,7,-10])

# print(aaaa)


# aaa11 = [1,1,2,2,2,2,3,3,3,4]
# aaa11.insert("")
# a111=min(aaa11)
# print("a1111",type(a111))
# b222 = max(aaa11)
# d = range(a111 , b222 )
# print(d)
# ddd= aaa11.count(1)
# n = 15
# list_a =range(n+1)

# print(list(list_a[1:16]))

# python = "Python is Amazing"
# print(python[0].isupper())
# print(python.replace("Python", "java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index+1)
# print(index)

# print(python.find("java")) #JAVA가 없으면 -1 출력해줌.

# test = 1234
# l = 3456
# l = str(l)
# l = list(l)
# l = set(l)
# # s = cmp(test, 0)
# # r = int('s*test'[::-1])
# # k = (r<2**31)*s*test
# # print(k)

# k = str(test)
# k = list(k)
# k = set(k)
# m = list(l&k)
# o = m[0]+m[1]
# print(o)
# print(type(m))

# k = 3
# nums = [1,2,3,4,5]
# # print(nums[-1])
# # nums.insert(0,nums[-1])
# # print(nums)
# # nums.pop(-1)
# # print(nums)
# while k > 0:
#     nums.insert(0,nums[-1])
    
#     nums.pop(-1)
#     print(nums)
#     k -= 1
nums = [3,0,1]
print(len(nums))
print(nums)
d = range(min(nums),max(nums)+1)
# print(len(d))
for i in d:
    print(i)

# d = range(min(nums),max(nums))
# print(d)
# # min = min(nums)
# # max = max(nums)
# if max(nums) == 0:
#     print("1")
# else:   
#     for i in d:
    
#         if i in set(nums):
#             pass
#         else:
#             print(i)