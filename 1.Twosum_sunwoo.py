class Sunwoo:
    def two_Sum(self, nums, target):
        hass = {}
        result = []
        
        
        for i , num in enumerate(nums):
            
            if hass.get(num) is None:
                hass[target - num] = i
            else:
                result = [hass[num], i]
        return result


s = Sunwoo()

d = s.two_Sum([1,2,3,5,9,5,4,3,6,7],15)
print(d)

