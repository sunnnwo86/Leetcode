class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)
        s = s[::-1]
        print(s)

s = Solution()
p = s.reverseString(["h","e","l","l","o"])
print(p)



# i = ["a","A","b","B","c","C"]
# print(i)
# i = i[::-1]
# print(i)