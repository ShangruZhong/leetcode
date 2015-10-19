"""
    24.Swap Nodes in Pairs
    @author: Shangru
    @date: 2015/10/19
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next:
            tmp = cur.next.next
            cur.next.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next.next
        return dummy.next





