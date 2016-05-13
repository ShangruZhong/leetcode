"""
	23. Merge k Sorted Lists

	@author: Shangru
	@date: 2016/05/12
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
    	if not lists:
    		return None
    	if len(lists) == 1:
    		return lists[0]
    	mid = len(lists)/2
    	left = self.mergeKLists(lists[:mid])
    	right = self.mergeKLists(lists[mid:])
    	return self.mergeTwoLists(left,right)
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(-1)
        p = dummy
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        if l1 != None:
            p.next = l1
        else:
            p.next = l2
        return dummy.next
