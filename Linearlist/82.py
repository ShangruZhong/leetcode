"""
    82. Remove Duplicates from Sorted List II

    @author: Shangru
    @date: 2015/10/16
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
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        flag = 0
        while head:
            if (head.next and head.next.next and head.next.next.val == head.next.val):
                head.next = head.next.next
                flag = 1
            elif flag and head.next:
                head.next = head.next.next #notice!
                flag = 0
            else:
                head = head.next
        return dummy.next

    # Solution 2
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
            if prev.next != head:
                prev.next = head.next
                head = prev.next
            else:    
                prev = head
                head = head.next
        return dummy.next 