"""
    142. Linked List Cycle II

    To find the circle head node (circle belongs to part of linked list):
    1. set fast, slow pointer, when fast = slow, they meet in the circle.
    2. set slow2 pointer from head of linked list, when slow = slow2,
        they meet at the head of circle, return circle head node.
        else return None. (Not false)
    3. do remember consider the none list  case and single node case, return None.
    @author: Shangru
    @date 2015/10/23
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: # Do remember !
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow2 = head
                while slow != slow2:
                    slow = slow.next
                    slow2 = slow2.next
                return slow2
        return None