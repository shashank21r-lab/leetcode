class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        maxx=0
        left=0

        for index , char in enumerate(s):
            if char in seen and seen[char]>=left:
                left=seen[char]+1
            seen[char]=index
            
            maxx=max(maxx,index-left+1)
        return maxx