"""
    141. Linked List Cycle

    To judge whether the linked list contains circle:
    1. set fast, slow pointer,
    2. when fast = slow,
        there must contain circle, return True.
        else return False

    @author: Shangru
    @date 2015/10/21
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
