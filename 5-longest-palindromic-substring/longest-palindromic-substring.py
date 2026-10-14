class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest=""

        for i in range(len(s)):
            for j in range(len(s)-1,i-1,-1):
                substring=s[i:j+1]
                
                if len(substring) > len(longest) and substring == substring[::-1]:
                    longest=substring     
        return longest