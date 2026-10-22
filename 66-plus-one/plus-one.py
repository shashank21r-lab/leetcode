class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number=0
        n=len(digits)
        for num in digits:
            number=(number*10)+num
        
        number=number+1
        res=[]
        while number > 0:
            digit=number%10
            res.append(digit)
            number=number // 10
        
        return res[::-1]