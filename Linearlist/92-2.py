"""
    92. Reverse Linked List II

    @date: 2017/01/09
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        for i in xrange(m - 1):
            prev = prev.next
        cur = prev.next
        reverse = None
        for i in xrange(n - m + 1):
            next = cur.next
            cur.next = reverse
            reverse = cur
            cur = next
        prev.next.next = cur
        prev.next = reverse
        return dummy.next