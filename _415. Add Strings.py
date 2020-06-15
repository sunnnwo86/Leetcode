class Solution:
    def addStrings(self, num1, num2):
        a = digits

        b = 10 **(len(a)-1) 

        
        c = 1
        d = 0
        while c <= len(a):

            for aa in a:

                b = 10 **(len(a)-(c))
                d += aa * b

                c += 1
        d += 1
        
        dd = str(d)

        dd = list(dd)
        
        f = 0
        while f <= len(dd)-1:
            for ddd in dd:
                dd[f] = int(ddd)
                f += 1
        return dd