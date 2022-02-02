# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        self.l1 = l1
        self.l2 = l2
        carry = False
        param = self.minLenCalc(l1,l2)
        if param[1] == 0: return self.sumaIguales(l1,l2)
        elif param[1] == 1:
            aux = self.l2
            self.l2 = self.l1
            self.l1 = aux
        solution_list = list()
        for i in range(param[2]):
            if i <= param[1]: suma = self.l1[i] + self.l2[i]
            else: suma = self.l1[i]
            if carry:
                suma +=1
                carry = False
            if suma > 9: 
                carry = True
                suma = suma%10
            solution_list.append(suma)
        if carry: solution_list.append(1)
        return solution_list
        
    def sumaIguales(self,l1,l2):
        solution_list = list()
        carry = False
        for i in range(len(l1)):
            suma = l1[i] + l2[i]
            if carry:
                suma +=1
                carry = False
            if suma > 9: 
                carry = True
                suma = suma%10
            solution_list.append(suma)
        if carry: solution_list.append(1)
        return solution_list

    def minLenCalc(self,l1,l2):
        if len(l1) > len(l2):       return [min(len(l1),len(l2)),-1, len(l1)]
        elif len(l1) == len(l2):    return [min(len(l1),len(l2)), 0, len(l1)]
        else:                       return [min(len(l1),len(l2)), 1, len(l2)]
        
