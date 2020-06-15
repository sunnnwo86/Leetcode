class Solution:
    def longestCommonPrefix(self, strs):
        
        if not strs:
            return ""
        shortest = min(strs,key=len)
        print(shortest)
        for i, ch in enumerate(shortest):
            print("i", i)
            print("ch", ch)
            for other in strs:
                if other[i] != ch:
                    print("shortest[:i]", shortest[:i])
                    return shortest[:i]
        return shortest 
    

s = Solution()  
p = s.longestCommonPrefix(["flower","flow","flight"])
print(p)