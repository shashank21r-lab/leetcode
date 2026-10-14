class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        new=0
        s=s.lstrip()

        if not s:
            return new
        if s[0].isdigit():
            sign=True
        elif s[0]=="-":
            sign=False
            s=s[1:]
        elif s[0]=='+':
            sign=True
            s=s[1:]
        else:
            return new
        
        for ch in s:
            if ch.isdigit():
                new=(new*10)+int(ch)
            else:
                break
        
        if not sign:
            new=new * -1
        
        if new < -2**31 :
            new=-2**31
        elif new > 2**31-1:
            new=2**31-1
        return new