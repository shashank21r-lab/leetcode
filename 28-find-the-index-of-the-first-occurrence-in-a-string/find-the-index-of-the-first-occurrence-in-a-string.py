class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)
        m=len(haystack)
        x=0
        y=n
        curr_word=haystack[x:y]

        for i in range(m):
            if curr_word==needle:
                return x
            x+=1
            y+=1
            curr_word=haystack[x:y]
        return -1