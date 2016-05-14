"""
    147. Insertion Sort List

    @date: 2016/05/14
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-10**10)
        cur = head
        while cur != None:
            pos = self.findInsertPos(dummy, cur.val)
            tmp = cur.next
            cur.next = pos.next
            pos.next = cur
            cur = tmp
        return dummy.next
        
    def findInsertPos(self, head, x):
        cur = head
        while cur != None and cur.val <= x:
            pre = cur
            cur = cur.next
        return pre