class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}

        for index , number in enumerate(nums):
            complement=target - number

            if complement in seen:
                return [seen[complement],index]
            
            seen[number]=index