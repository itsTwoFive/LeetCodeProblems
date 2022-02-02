class Solution(object):
    def findLonely(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        solution_list = list()
        for element in nums:
            if nums.count(element) == 1 and nums.count(element-1) == 0 and nums.count(element+1) == 0:
                solution_list.append(element)
        return solution_list
