class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res=num[s[-1]]

        for i in range(len(s)-1):
            if num[s[i]] < num[s[i+1]]:
                res-=num[s[i]]
            else:
                res+=num[s[i]] 
        return res