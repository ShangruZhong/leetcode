"""
    25. Reverse Nodes in k-Group

    Similar to 24.Swap Nodes in Pairs, while k=2.
    Reverse once every k nodes.
    Remain while number of resting node < k.

    @author: Shangru
    @date: 2015/10/20
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while k and cur.next and cur.next:
            tmp = cur.next.next
            cur.next.next = tmp.next
            tmp.next = cur.next
            cur.next = tmp
            cur = cur.next
            k -= 1