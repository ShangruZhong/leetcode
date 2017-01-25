"""
    83. Remove Duplicates from Sorted List

    @author: Shangru
    @date: 2015/10/15
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        pend = cur.next
        while pend:
            while cur.val == pend.val:
                pend = pend.next
                if pend == None:
                    break
            cur.next = pend
            cur = cur.next
            if pend != None:
                pend = pend.next
        return head

    # Solution 2
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next != head:
                prev.next = head
            prev = head
            head = head.next
        return dummy.next