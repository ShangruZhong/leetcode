"""
    19. Remove Nth Node From End of List

    @author: Shangru
    @date: 2015/10/15
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        if n==length:
            return head.next
        else:
            last = head
            for i in range(length-n-1):
                last = last.next
            remove = last.next
            if remove.next:
                last.next = remove.next
            else:
                last.next = None
            return head

