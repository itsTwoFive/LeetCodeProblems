class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        actual_sum = sum(nums)
        max_sum = actual_sum
        solutions = [0]
        for i in range(1,len(nums)+1): 
            if nums[i-1] == 0: actual_sum +=1
            elif nums[i-1] == 1: actual_sum -=1
            if actual_sum > max_sum:
                solutions = [i]
                max_sum = actual_sum
            elif actual_sum == max_sum: solutions.append(i)
        return solutions

