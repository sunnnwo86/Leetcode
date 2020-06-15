class Solution:
    def reverse(self, x):
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
            return x*(x<2**31)
        
        else:
            x = str(x)
            x = "-"+ x[:0:-1]
            x = int(x)
            return x*(x<2**31)
        

s = Solution()

p = s.reverse(-120) 
print(p)

