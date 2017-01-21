"""
	203. Remove Linked List Elements

	@date: 2017/01/21
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            if head.val == val:
                prev.next = head.next
                head = prev.next
            else:
                head = head.next
                prev = prev.next
        return dummy.next