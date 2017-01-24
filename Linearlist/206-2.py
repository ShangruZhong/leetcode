"""
    206. Reverse Linked List

    @date: 2017/01/09
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, pend = None, None
        while head:
            pend = head.next
            head.next = prev
            prev = head
            head = pend
        return prev