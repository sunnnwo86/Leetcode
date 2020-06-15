# 9. Palindrome Number
# 앞뒤가 똑같은 숫자 구분.
#12321
class Solution:
    def isPalindrome(self, x):
        
        b = str(x)
        if b == b[::-1]:
            return True
        else:
            return False


s = Solution()
s.isPalindrome(121)
print(s.isPalindrome(1212))

