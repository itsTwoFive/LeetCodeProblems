class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        max = 0
        max_list = list()
        for i in range(0,n+1):
            actual_left = 0
            actual_right = 0
            for j in range(0,i):
                if nums[j]==0:
                    actual_left +=1
            for j in range(i,n):
                if nums[j]==1:
                    actual_right +=1
            actual = actual_right + actual_left
            if actual == max:
                max_list.append(i)
            elif actual > max:
                max_list = [i]
                max = actual
        
        return max_list

