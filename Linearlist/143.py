"""
    143. Reorder List

    Find middle pointer & reverse latter half list
    Merge two linked list
    @date: 2017/01/20
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None:
            return head
        mid = self.findMiddle(head)
        tail = self.reverseList(mid.next)
        cur = head
        mid.next = None
        while tail and cur:
            p1 = cur.next
            cur.next = tail
            p2 = tail.next
            tail.next = p1
            cur = p1
            tail = p2
        
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev = None
        next = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev