class Solution:
    def fizzBuzz(self, n):
        # list_a =range(n+1)
        # print(list(list_a[1:16]))
        
        ss= []
        
        a = range(n+1)
        
        for s in a[1:n+1]:
            if s%15 == 0:
                ss.insert(s,"FizzBuzz")
            elif s%5 == 0:
                ss.insert(s,"Buzz")
            elif s%3 == 0:
                ss.insert(s,"Fizz")
            else:
                ss.insert(s,str(s))
        return ss,print(ss)
s = Solution()
p = s.fizzBuzz(15)