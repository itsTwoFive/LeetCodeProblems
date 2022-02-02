class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        for element in nums:
            if element == original:
                return self.findFinalValue(nums,original*2)
        return original