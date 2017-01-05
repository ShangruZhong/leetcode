"""
    160. Intersection of Two Linked Lists

    Straight-forward
    @date: 2017/01/05
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return None

        p1, p2 = headA, headB
        len1, len2 = 0, 0
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        p1, p2 = headA, headB
        if len1 >= len2:
            n = len1 - len2
            while n:
                p1 = p1.next
                n -= 1
        else:
            n = len2 - len1
            while n:
                p2 = p2.next
                n -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1