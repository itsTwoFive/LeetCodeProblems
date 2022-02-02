class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        min_num = min(nums)
        count = 0
        for elem in nums:
            if elem > min_num and elem < max_num: count+=1
        return count
