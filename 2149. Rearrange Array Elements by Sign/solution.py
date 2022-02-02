class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list_negative = list()
        list_positive = list()
        list_final = list()
        for elem in nums:
            if elem < 0: list_negative.append(elem)
            else: list_positive.append(elem)
        for i in range(len(list_positive)):
            list_final.append(list_positive[i])
            list_final.append(list_negative[i])
        return list_final