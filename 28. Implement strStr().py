class Solution:
    def strStr(self, haystack, needle):
        
        if haystack.find(needle) != -1:
            return haystack.find(needle)
        else:
            return haystack.find(needle)


s = Solution() 
p = s.strStr("apple","aa")
print(p)
